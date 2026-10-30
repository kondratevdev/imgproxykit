from dataclasses import dataclass
from typing import Annotated, Final

from imgproxykit import Client, Transform
from tests.fixtures.credentials import Credentials

_SOURCE: Final = 'https://example.com/photo.jpg'


@dataclass(frozen=True, slots=True)
class _ImageVariants:
    """Declare one reusable result shape for different sources and clients."""

    small: Annotated[str, Transform(width=320)]
    original: Annotated[str, Transform()]


def test_different_sources() -> None:
    """Reuse a declaration without retaining URLs from an earlier source."""
    client = Client('https://example.com')
    other_source = 's3://bucket/other.jpg'

    first = client.variants(_SOURCE, variants=_ImageVariants)
    other = client.variants(other_source, variants=_ImageVariants)

    assert first == _ImageVariants(
        small=client.url(_SOURCE, transform=Transform(width=320)),
        original=client.url(_SOURCE),
    )
    assert other == _ImageVariants(
        small=client.url(other_source, transform=Transform(width=320)),
        original=client.url(other_source),
    )


def test_different_clients(credentials: Credentials) -> None:
    """Keep the host and signing settings specific to each client."""
    unsigned = Client('https://unsigned.example.com')
    signed = Client('https://signed.example.com', **credentials)

    first = unsigned.variants(_SOURCE, variants=_ImageVariants)
    other = signed.variants(_SOURCE, variants=_ImageVariants)

    assert first == _ImageVariants(
        small=unsigned.url(_SOURCE, transform=Transform(width=320)),
        original=unsigned.url(_SOURCE),
    )
    assert other == _ImageVariants(
        small=signed.url(_SOURCE, transform=Transform(width=320)),
        original=signed.url(_SOURCE),
    )


def test_fresh_instances() -> None:
    """Return equal but independent instances for identical arguments."""
    client = Client('https://example.com')

    first = client.variants(_SOURCE, variants=_ImageVariants)
    repeated = client.variants(_SOURCE, variants=_ImageVariants)

    assert first == repeated
    assert first is not repeated
