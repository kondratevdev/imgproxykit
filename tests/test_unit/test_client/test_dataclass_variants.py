from dataclasses import dataclass
from typing import Annotated, Final, assert_type

from imgproxykit import Client, Transform
from tests.fixtures.credentials import Credentials

_SOURCE: Final = 'https://example.com/photo.jpg'


@dataclass(frozen=True, slots=True, kw_only=True)
class _ImageVariants:
    """Provide typed URL fields for client integration checks."""

    small: Annotated[str, Transform(width=320)]
    original: Annotated[str, Transform()]


@dataclass(frozen=True, slots=True)
class _EmptyVariants:
    """Declare an empty result."""


def test_dataclass_variants() -> None:
    """Return the declared dataclass with generated URLs in its fields."""
    images = Client('https://example.com').variants(
        _SOURCE,
        variants=_ImageVariants,
    )

    assert_type(images, _ImageVariants)
    assert_type(images.small, str)
    assert images == _ImageVariants(
        small='https://example.com/unsafe/width:320/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        original='https://example.com/unsafe/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_signed_dataclass_variants(credentials: Credentials) -> None:
    """Use the client's signing and source encoding for every variant."""
    client = Client(
        'https://example.com',
        source_encoding='plain',
        **credentials,
    )

    images = client.variants(_SOURCE, variants=_ImageVariants)

    assert images == _ImageVariants(
        small=client.url(_SOURCE, transform=Transform(width=320)),
        original=client.url(_SOURCE),
    )


def test_empty_dataclass_variants() -> None:
    """Construct a result when the declaration has no fields."""
    client = Client('https://example.com')

    assert client.variants(_SOURCE, variants=_EmptyVariants) == _EmptyVariants()
