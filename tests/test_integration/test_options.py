from typing import Final

import pytest
import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Background, Crop, Flip, Format, Padding
from tests.test_integration.assertions import assert_image

_SOURCE: Final = 'local:///pattern.png'
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
    colors: tuple[tuple[int, int, int], ...],
) -> None:
    """Ensure that flip axes affect the expected image quadrants."""
    transform = Transform(option, Format('png'))
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(
        response,
        format='PNG',
        size=(80, 60),
        pixels=dict(zip(_POSITIONS, colors, strict=True)),
    )


def test_crop(imgproxy_client: Client, http_client: zapros.Client) -> None:
    """Ensure that crop gravity selects the bottom right source quadrant."""
    transform = Transform(
        Crop(width=_CROP_WIDTH, height=_CROP_HEIGHT, gravity='soea'),
        Format('png'),
    )
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(
        response,
        format='PNG',
        size=(_CROP_WIDTH, _CROP_HEIGHT),
        pixels={(10, 10): _YELLOW, (30, 20): _YELLOW},
    )


def test_padding(imgproxy_client: Client, http_client: zapros.Client) -> None:
    """Ensure that padding follows CSS side order and uses the background."""
    transform = Transform(
        Padding(top=1, right=2, bottom=3, left=4),
        Background(color='ffffff'),
        Format('png'),
    )
    url = imgproxy_client.url(_SOURCE, transform=transform)

    response = http_client.get(url)

    assert_image(
        response,
        format='PNG',
        size=(86, 64),
        pixels={
            (0, 0): (255, 255, 255),
            (3, 10): (255, 255, 255),
            (4, 1): _RED,
            (83, 60): _YELLOW,
            (84, 10): (255, 255, 255),
            (10, 61): (255, 255, 255),
        },
    )


@pytest.mark.parametrize('color', ['0000ff', _BLUE])
def test_background(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    color: str | tuple[int, int, int],
) -> None:
    """Ensure that both background forms fill transparent source pixels."""
    transform = Transform(Background(color=color), Format('png'))
    url = imgproxy_client.url('local:///transparent.png', transform=transform)

    response = http_client.get(url)

    assert_image(
        response,
        format='PNG',
        size=(80, 60),
        pixels={(0, 0): _BLUE, (40, 30): _RED},
    )
