from collections.abc import Mapping
from dataclasses import asdict, is_dataclass
from typing import TYPE_CHECKING, overload

from django.db.models.fields.files import FieldFile

from imgproxykit.integrations.django.client import get_client
from imgproxykit.integrations.django.settings import Settings, get_config
from imgproxykit.integrations.django.sources import resolve_source
from imgproxykit.internal.types import VariantsResult
from imgproxykit.transform import Transform

if TYPE_CHECKING:
    from _typeshed import DataclassInstance


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
def imgproxy_variants(
    source: str | FieldFile,
    variants: str,
) -> dict[str, str]: ...


@overload
def imgproxy_variants[Key: str](
    source: str | FieldFile,
    variants: Mapping[Key, Transform],
) -> dict[Key, str]: ...


@overload
def imgproxy_variants[VariantSet: DataclassInstance](
    source: str | FieldFile,
    variants: type[VariantSet],
) -> VariantSet: ...


def imgproxy_variants[Key: str](
    source: str | FieldFile,
    variants: Mapping[Key, Transform] | type['DataclassInstance'] | str,
) -> VariantsResult[Key]:
    """
    Build named image URLs using Django's configured client.

    Args:
        source: Source URI or model file field, resolved once for all variants.
        variants: Transformation mapping, dataclass class,
            or set name from ``IMGPROXYKIT['variants']``.

    Returns:
        URLs in variant order. Direct mappings preserve their key type.
        Dataclass classes passed directly produce instances of that class.
        Named sets always produce dictionaries of URLs.

    Raises:
        KeyError: If a named variant set is not configured.
        ValueError: If the default source resolver receives an empty file field.
    """
    client = get_client()

    # 1. For a mapping or dataclass class, return the client result as is.
    # 2. For a set name, read its declaration from settings first.
    # 3. Resolve the source once, then build the URLs.
    # 4. Always return a dict for a set name, even if it uses a dataclass.
    if not isinstance(variants, str):
        return client.variants(resolve_source(source), variants=variants)

    configured = get_config()[Settings.variants.value][variants]  # pyright: ignore[reportTypedDictNotRequiredAccess]
    images = client.variants(resolve_source(source), variants=configured)
    return asdict(images) if is_dataclass(images) else images
