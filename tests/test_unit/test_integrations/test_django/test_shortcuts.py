from dataclasses import dataclass
from typing import Annotated, Final, assert_type

from django.conf import LazySettings
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


@dataclass(frozen=True, slots=True)
class _Images:
    """Declare typed image variants for Django and DRF."""

    small: Annotated[str, Transform(width=160)]


def test_dataclass_variants(settings: LazySettings) -> None:
    """Preserve direct dataclasses and return dictionaries for named sets."""
    settings.IMGPROXYKIT = {
        'client': {'base_url': 'https://example.com'},
        'variants': {'product': _Images},
    }
    source = 'https://example.com/photo.jpg'

    images = imgproxy_variants(source, _Images)
    assert_type(images, _Images)
    assert images == snapshot(
        _Images(
            small='https://example.com/unsafe/width:160/'
            'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        )
    )

    urls = imgproxy_variants(source, 'product')
    assert_type(urls, dict[str, str])
    assert urls == {'small': images.small}
