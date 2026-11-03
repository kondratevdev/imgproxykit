from typing import Final

import pytest
import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Background, Crop, Flip, Gravity, Padding
from tests.test_integration.test_imgproxy.assertions import (
    Color,
    Position,
    Size,
    assert_image,
)

_SOURCE: Final = 'local:///color-quadrants-80x60.png'
_WHITE: Final = (255, 255, 255)
_RED: Final = (255, 0, 0)
_GREEN: Final = (0, 255, 0)
_BLUE: Final = (0, 0, 255)
_YELLOW: Final = (255, 255, 0)
_CROP_WIDTH: Final = 40
_CROP_HEIGHT: Final = 30
_POSITIONS: Final = (
    (10, 10),
    (70, 10),
    (10, 50),
    (70, 50),
)


@pytest.mark.parametrize(
    ('option', 'colors'),
    [
        (Flip(horizontal=True), (_GREEN, _RED, _YELLOW, _BLUE)),
        (Flip(vertical=True), (_BLUE, _YELLOW, _RED, _GREEN)),
        (Flip(horizontal=False, vertical=True), (_BLUE, _YELLOW, _RED, _GREEN)),
        (Flip(horizontal=True, vertical=True), (_YELLOW, _BLUE, _GREEN, _RED)),
    ],
)
def test_flip(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    option: Flip,
    colors: tuple[Color, ...],
) -> None:
    """Ensure that flip axes affect the expected image quadrants."""
    transform = Transform(option, format='png')
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(
        response,
        size=(80, 60),
        pixels=dict(zip(_POSITIONS, colors, strict=True)),
    )


@pytest.mark.parametrize(
    ('gravity', 'color'),
    [
        (Gravity.top_left(), _RED),
        (Gravity.top_right(), _GREEN),
        (Gravity.bottom_left(), _BLUE),
        (Gravity.bottom_right(), _YELLOW),
    ],
)
def test_crop(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    gravity: Gravity,
    color: Color,
) -> None:
    """Ensure that gravity factories select the expected source quadrant."""
    transform = Transform(
        Crop(width=_CROP_WIDTH, height=_CROP_HEIGHT, gravity=gravity),
        format='png',
    )
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(
        response,
        size=(_CROP_WIDTH, _CROP_HEIGHT),
        pixels={(10, 10): color, (30, 20): color},
    )


@pytest.mark.parametrize(
    ('padding', 'size', 'pixels'),
    [
        (
            Padding(top=1, right=2, bottom=3, left=4),
            (86, 64),
            {
                (0, 0): _WHITE,
                (3, 10): _WHITE,
                (4, 1): _RED,
                (83, 60): _YELLOW,
                (84, 10): _WHITE,
                (10, 61): _WHITE,
            },
        ),
        (
            Padding.all(2),
            (84, 64),
            {
                (10, 1): _WHITE,
                (1, 10): _WHITE,
                (2, 2): _RED,
                (81, 61): _YELLOW,
                (82, 10): _WHITE,
                (10, 62): _WHITE,
            },
        ),
        (
            Padding.symmetric(horizontal=3, vertical=2),
            (86, 64),
            {
                (10, 1): _WHITE,
                (2, 10): _WHITE,
                (3, 2): _RED,
                (82, 61): _YELLOW,
                (83, 10): _WHITE,
                (10, 62): _WHITE,
            },
        ),
    ],
)
def test_padding(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    padding: Padding,
    size: Size,
    pixels: dict[Position, Color],
) -> None:
    """Ensure that padding constructors and factories place all four edges."""
    transform = Transform(padding, Background.hex('ffffff'), format='png')
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(response, size=size, pixels=pixels)


@pytest.mark.parametrize(
    'background',
    [
        Background(color='0000ff'),
        Background(color=_BLUE),
        Background.hex('0000ff'),
        Background.rgb(red=0, green=0, blue=255),
    ],
)
def test_background(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    background: Background,
) -> None:
    """Ensure that background constructors and factories fill transparency."""
    transform = Transform(background, format='png')
    url = imgproxy_client.url(
        'local:///red-center-transparent-80x60.png',
        transform=transform,
    )

    response = http_client.get(url)

    assert_image(
        response,
        size=(80, 60),
        pixels={(0, 0): _BLUE, (40, 30): _RED},
    )
