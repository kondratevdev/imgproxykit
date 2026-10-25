from typing import Final

from inline_snapshot import snapshot

from imgproxykit import Transform
from imgproxykit.integrations.django import imgproxy_url, imgproxy_variants

_SOURCE: Final = 'https://example.com/photo.jpg'


def test_url_without_transform() -> None:
    """Build a URL without processing options when no transform is given."""
    assert imgproxy_url(_SOURCE) == snapshot(
        'https://example.com/unsafe/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_url_with_transform() -> None:
    """Apply a directly supplied transformation to the URL."""
    assert imgproxy_url(_SOURCE, Transform(width=160)) == snapshot(
        'https://example.com/unsafe/width:160/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_variants() -> None:
    """Build URLs from a directly supplied variant mapping."""
    urls = imgproxy_variants(
        _SOURCE,
        {
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
