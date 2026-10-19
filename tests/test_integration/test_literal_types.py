from http import HTTPStatus
from typing import Final, get_args

import pytest
import zapros

from imgproxykit import Client, Transform, options
from imgproxykit.types import (
    EMPTY,
    FormatType,
    Position,
    ResizeType,
    WatermarkPosition,
)
from tests.test_integration.assertions import assert_image

_SOURCE: Final = 'local:///pattern.png'
_WIDTH: Final = 80
_HEIGHT: Final = 60


# Every built-in option is sent to imgproxy to check that its name is valid
# and works with real arguments.
@pytest.mark.parametrize(
    'option',
    [
        options.Format('png'),
        options.Width(value=_WIDTH),
        options.Height(value=_HEIGHT),
        options.MinWidth(value=0),
        options.MinHeight(value=0),
        options.ResizingType(value='fit'),
        options.Enlarge(value=False),
        options.AutoRotate(value=True),
        options.Rotate(value=0),
        options.Blur(value=0),
        options.Sharpen(value=0),
        options.Pixelate(value=0),
        options.StripMetadata(value=True),
        options.KeepCopyright(value=False),
        options.StripColorProfile(value=True),
        options.PreserveHDR(value=False),
        options.EnforceThumbnail(value=False),
        options.MaxBytes(value=0),
        options.Raw(value=False),
        options.Expires(value=0),
        options.ReturnAttachment(value=False),
        options.MaxSrcResolution(value=1),
        options.MaxSrcFileSize(value=0),
        options.MaxAnimationFrames(value=1),
        options.MaxAnimationFrameResolution(value=1),
        options.MaxResultDimension(value=0),
        options.Size(width=_WIDTH, height=_HEIGHT),
        options.Zoom(factor_x=1),
        options.Extend(value=False),
        options.ExtendAspectRatio(value=False),
        options.Crop(width=_WIDTH, height=_HEIGHT),
        options.Trim(threshold=0),
        options.Padding(top=0),
        options.Flip(horizontal=False),
        options.Background(color='ffffff'),
        options.FormatQuality(qualities=(('png', 1),)),
        options.SkipProcessing(formats=('png',)),
        options.Filename(value='image'),
        options.CacheBuster(value='v1'),
        options.Resize(width=_WIDTH, height=_HEIGHT, mode='fit'),
        options.Gravity(position='ce'),
        options.DPR(1),
        options.Quality(1),
        options.Watermark(opacity=1),
    ],
)
def test_option_type(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    option: options.Option,
) -> None:
    """Ensure that imgproxy recognizes every declared option name."""
    url = imgproxy_client.url(
        _SOURCE,
        transform=Transform(option),
    )

    response = http_client.get(url)
    assert_image(response.read(), size=(_WIDTH, _HEIGHT))


@pytest.mark.parametrize('output_format', get_args(FormatType.__value__))
def test_format_type(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    output_format: FormatType,
) -> None:
    """Ensure that format names are recognized without requiring encoders."""
    transform = Transform(
        options.FormatQuality(qualities=((output_format, 1),)),
    )
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)
    assert_image(response.read(), size=(_WIDTH, _HEIGHT))


@pytest.mark.parametrize('position', get_args(Position.__value__))
def test_position(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    position: Position,
) -> None:
    """Ensure that imgproxy accepts every declared crop gravity."""
    transform = Transform(
        options.Crop(
            width=_WIDTH,
            height=_HEIGHT,
            gravity=position,
            offset_x=0.5 if position == 'fp' else EMPTY,
            offset_y=0.5 if position == 'fp' else EMPTY,
        ),
    )
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(response.read(), size=(_WIDTH, _HEIGHT))


@pytest.mark.parametrize('mode', get_args(ResizeType.__value__))
def test_resize_type(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    mode: ResizeType,
) -> None:
    """Ensure that imgproxy accepts every declared resizing strategy."""
    transform = Transform(
        options.Resize(width=_WIDTH, height=_HEIGHT, mode=mode),
    )
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(response.read(), size=(_WIDTH, _HEIGHT))


@pytest.mark.parametrize('position', get_args(WatermarkPosition.__value__))
def test_watermark_position(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    position: WatermarkPosition,
) -> None:
    """Ensure that imgproxy accepts every declared watermark position."""
    transform = Transform(
        options.Watermark(opacity=1, position=position),
    )
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(response.read(), size=(_WIDTH, _HEIGHT))


def test_invalid_literal_value(
    imgproxy_client: Client,
    http_client: zapros.Client,
) -> None:
    """Ensure that the server rejects invalid literals in the test setup."""
    # Bypass typing for one negative control of the acceptance tests above.
    option = options.Resize(mode='invalid')  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
    transform = Transform(option)
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert response.status == HTTPStatus.NOT_FOUND
    assert response.text == 'Invalid URL'
