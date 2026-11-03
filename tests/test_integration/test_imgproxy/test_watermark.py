from typing import Final, get_args

import pytest
import zapros

from imgproxykit import Client, Transform, options
from imgproxykit.types import WatermarkPosition
from tests.fixtures.imgproxy import override_imgproxy_env
from tests.test_integration.test_imgproxy.assertions import assert_image

_SOURCE: Final = 'local:///color-quadrants-80x60.png'
_WIDTH: Final = 80
_HEIGHT: Final = 60


@override_imgproxy_env(
    IMGPROXY_WATERMARK_PATH='/data/images/red-center-transparent-80x60.png',
)
def test_watermark_option_type(
    imgproxy_client: Client,
    http_client: zapros.Client,
) -> None:
    """Ensure that imgproxy recognizes the configured watermark option."""
    url = imgproxy_client.url(
        _SOURCE,
        transform=Transform(options.Watermark(opacity=1)),
    )

    response = http_client.get(url)

    assert_image(response, size=(_WIDTH, _HEIGHT))


@override_imgproxy_env(
    IMGPROXY_WATERMARK_PATH='/data/images/red-center-transparent-80x60.png',
)
@pytest.mark.parametrize('position', get_args(WatermarkPosition.__value__))
def test_watermark_position(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    position: WatermarkPosition,
) -> None:
    """Ensure that imgproxy accepts every declared watermark position."""
    transform = Transform(options.Watermark(opacity=1, position=position))
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(response, size=(_WIDTH, _HEIGHT))
