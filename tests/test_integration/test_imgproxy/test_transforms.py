from typing import Final

import pytest
import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Gravity, Resize
from imgproxykit.types import FormatType
from tests.test_integration.test_imgproxy.assertions import (
    Color,
    Position,
    Size,
    assert_image,
)

_WIDTH: Final = 160
_HEIGHT: Final = 120
_RED: Final = (255, 0, 0)
_GREEN: Final = (0, 255, 0)
_BLUE: Final = (0, 0, 255)


@pytest.mark.parametrize(
    ('output_format', 'expected_format', 'content_type'),
    [
        ('webp', 'WEBP', 'image/webp'),
        ('png', 'PNG', 'image/png'),
        ('jpg', 'JPEG', 'image/jpeg'),
    ],
)
def test_signed_resize(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    output_format: FormatType,
    expected_format: str,
    content_type: str,
) -> None:
    """Ensure that signed transforms select the expected size and format."""
    transform = Transform(
        Resize(width=_WIDTH, height=_HEIGHT, mode='fill'),
        format=output_format,
    )
    url = imgproxy_client.url(
        'local:///solid-red-640x480.png',
        transform=transform,
    )

    response = http_client.get(url)

    assert response.headers['Content-Type'] == content_type
    assert_image(
        response,
        format=expected_format,
        size=(_WIDTH, _HEIGHT),
    )


def test_resize_height(
    imgproxy_client: Client,
    http_client: zapros.Client,
) -> None:
    """Ensure that omitted resize arguments preserve source proportions."""
    transform = Transform(Resize(height=_HEIGHT))
    url = imgproxy_client.url(
        'local:///solid-red-640x480.png',
        transform=transform,
    )

    response = http_client.get(url)

    assert_image(response, size=(_WIDTH, _HEIGHT))


@pytest.mark.parametrize(
    ('resize', 'size', 'pixels'),
    [
        (
            Resize.fit(width=40, height=40),
            (40, 30),
            {(23, 5): _GREEN, (10, 25): _BLUE},
        ),
        (
            Resize.fill(width=40, height=40),
            (40, 40),
            {(23, 5): _RED, (10, 25): _BLUE},
        ),
        (
            Resize.force(width=40, height=40),
            (40, 40),
            {(23, 5): _GREEN, (10, 25): _BLUE},
        ),
    ],
)
def test_resize_factories(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    resize: Resize,
    size: Size,
    pixels: dict[Position, Color],
) -> None:
    """Ensure that resize factories fit, crop, or stretch source quadrants."""
    # Top-left fill keeps the red/green boundary near x=27; force uses x=20.
    transform = Transform(resize, Gravity.top_left(), format='png')
    url = imgproxy_client.url(
        'local:///color-quadrants-80x60.png',
        transform=transform,
    )

    response = http_client.get(url)

    assert_image(response, size=size, format='PNG', pixels=pixels)
