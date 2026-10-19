from typing import Final

import pytest
from inline_snapshot import snapshot

from imgproxykit import Client, Transform
from imgproxykit.options import Preset, Resize

_SOURCE: Final = 'https://example.com/photo.jpg'
_WIDTH: Final = 300
_HEIGHT: Final = 200


@pytest.mark.parametrize(
    'base_url',
    [
        'https://example.com/images',
        'https://example.com/images/',
        'https://example.com/images///',
    ],
)
def test_unsigned_url(*, base_url: str) -> None:
    """Ensure that base URL prefixes survive trailing slash removal."""
    client = Client(base_url)

    assert client.url(_SOURCE) == snapshot(
        'https://example.com/images/unsafe/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_signed_url() -> None:
    """Ensure that the complete processing path is signed."""
    client = Client(
        'https://example.com',
        key='736563726574',
        salt='73616c74',
    )
    transform = Transform(
        Resize(
            width=_WIDTH,
            height=_HEIGHT,
            mode='fill',
        ),
        format='webp',
    )

    assert client.url(_SOURCE, transform=transform) == snapshot(
        'https://example.com/'
        '9TG79qV8tG6YeCbuGRKt1eLM9SySuCJAldwf3zcrlJU/'
        'resize:fill:300:200/format:webp/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_presets_url() -> None:
    """Ensure that preset names and output format reach the path builder."""
    client = Client('https://example.com')

    assert client.url(
        _SOURCE,
        transform=Transform(
            Preset(names=('thumbnail', 'watermarked')),
            format='avif',
        ),
    ) == snapshot(
        'https://example.com/unsafe/preset:thumbnail:watermarked/format:avif/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )
