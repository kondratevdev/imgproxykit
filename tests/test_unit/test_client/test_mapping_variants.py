from collections.abc import Callable, Mapping
from types import MappingProxyType
from typing import Final, Literal, assert_type

import pytest
from inline_snapshot import snapshot

from imgproxykit import Client, Transform

_SOURCE: Final = 'https://example.com/photo.jpg'

type _VariantKeys = Literal['small', 'large']
type _MappingFactory = Callable[
    [dict[_VariantKeys, Transform]],
    Mapping[_VariantKeys, Transform],
]


@pytest.mark.parametrize('mapping_factory', [dict, MappingProxyType])
def test_variants(*, mapping_factory: _MappingFactory) -> None:
    """Ensure that each variant name maps to its transformed URL."""
    client = Client('https://example.com')
    transforms: dict[_VariantKeys, Transform] = {
        'small': Transform(width=320),
        'large': Transform(width=1280),
    }
    variants = mapping_factory(transforms)

    urls = client.variants(_SOURCE, variants=variants)

    assert_type(urls, dict[_VariantKeys, str])
    assert urls == snapshot({
        'small': 'https://example.com/unsafe/width:320/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        'large': 'https://example.com/unsafe/width:1280/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    })
    assert list(urls) == ['small', 'large']
    assert dict(variants) == transforms


def test_empty_variants() -> None:
    """Ensure that an empty variant mapping produces no URLs."""
    client = Client('https://example.com')

    assert client.variants(_SOURCE, variants={}) == {}
