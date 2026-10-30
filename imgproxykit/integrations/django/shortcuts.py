from collections.abc import Mapping
from typing import overload

from django.db.models.fields.files import FieldFile

from imgproxykit.integrations.django.client import get_client
from imgproxykit.integrations.django.settings import Settings, get_config
from imgproxykit.integrations.django.sources import resolve_source
from imgproxykit.transform import Transform


def imgproxy_url(
    source: str | FieldFile,
    transform: Transform | str | None = None,
) -> str:
    """
    Build an imgproxy URL using Django's configured client.

    Args:
        source: Source URI or model file field, passed to the source resolver.
        transform: Transformation or name from ``IMGPROXYKIT['transforms']``.
            Omit to add no processing options.

    Returns:
        Image URL.

    Raises:
        KeyError: If a named transformation is not configured.
        ValueError: If the default source resolver receives an empty file field.
    """
    if isinstance(transform, str):
        transform = get_config()[Settings.transforms.value][transform]  # pyright: ignore[reportTypedDictNotRequiredAccess]
    return get_client().url(resolve_source(source), transform=transform)


@overload
def imgproxy_variants[Key: str](
    source: str | FieldFile,
    variants: Mapping[Key, Transform],
) -> dict[Key, str]: ...


@overload
def imgproxy_variants(
    source: str | FieldFile,
    variants: str,
) -> dict[str, str]: ...


def imgproxy_variants[Key: str](
    source: str | FieldFile,
    variants: Mapping[Key, Transform] | str,
) -> dict[Key, str] | dict[str, str]:
    """
    Build named image URLs using Django's configured client.

    Args:
        source: Source URI or model file field, resolved once for all variants.
        variants: Transformation mapping or set name from
            ``IMGPROXYKIT['variants']``.

    Returns:
        URLs in variant order. Direct mappings preserve their key type.

    Raises:
        KeyError: If a named variant set is not configured.
        ValueError: If the default source resolver receives an empty file field.
    """
    client = get_client()

    # Resolve the source inside each branch so named sets are looked up first.
    # Only one branch runs, so the resolver is called once per invocation.
    if not isinstance(variants, str):
        return client.variants(resolve_source(source), variants=variants)

    configured = get_config()[Settings.variants.value][variants]  # pyright: ignore[reportTypedDictNotRequiredAccess]
    return client.variants(resolve_source(source), variants=configured)
