from typing import Final

import pytest
from inline_snapshot import snapshot

from imgproxykit import Client, Transform
from imgproxykit.options import Resize
from tests.fixtures.credentials import Credentials

_SOURCE: Final = 'https://example.com/photo.jpg'


def test_signed_plain_url(credentials: Credentials) -> None:
    """Sign the escaped source, plain marker, and processing options."""
    client = Client(
        'https://example.com/images',
        source_encoding='plain',
        **credentials,
    )

    assert client.url(
        'http://example.com/images/curiosity.jpg?size=300',
        transform=Transform(format='webp'),
    ) == (
        'https://example.com/images/'
        '0s1_Nbh2MUZKyCQSiyR84xwesu69AYqKEYO_ux_Qgc8/'
        'format:webp/plain/'
        'http%3A%2F%2Fexample.com%2Fimages%2Fcuriosity.jpg%3Fsize%3D300'
    )


@pytest.mark.parametrize(
    'base_url',
    [
        # A prefix without a trailing slash is preserved.
        'https://example.com/images',
        # A single trailing slash is removed.
        'https://example.com/images/',
        # Multiple trailing slashes are removed.
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


def test_signed_url(credentials: Credentials) -> None:
    """Ensure that the complete processing path is signed."""
    client = Client(
        'https://example.com',
        **credentials,
    )
    transform = Transform(
        Resize(width=300, height=200, mode='fill'),
        format='webp',
    )

    assert client.url(_SOURCE, transform=transform) == snapshot(
        'https://example.com/'
        '9TG79qV8tG6YeCbuGRKt1eLM9SySuCJAldwf3zcrlJU/'
        'resize:fill:300:200/format:webp/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_variants() -> None:
    """Ensure that each variant name maps to its transformed URL."""
    client = Client('https://example.com')

    urls = client.variants(
        _SOURCE,
        variants={
            'small': Transform(width=320),
            'large': Transform(width=1280),
        },
    )

    assert urls == snapshot({
        'small': 'https://example.com/unsafe/width:320/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        'large': 'https://example.com/unsafe/width:1280/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    })


def test_empty_variants() -> None:
    """Ensure that an empty variant mapping produces no URLs."""
    client = Client('https://example.com')

    assert client.variants(_SOURCE, variants={}) == {}
