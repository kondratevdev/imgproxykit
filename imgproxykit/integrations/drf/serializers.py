from collections.abc import Mapping
from typing import Any, override

from django.db.models.fields.files import FieldFile
from rest_framework import serializers

from imgproxykit.integrations.django import imgproxy_url, imgproxy_variants
from imgproxykit.transform import Transform


class ImgproxyURLField(serializers.URLField):
    """
    Represent a source string or model file as a read-only imgproxy URL.

    Use Django's ``IMGPROXYKIT`` settings without request context. Empty
    sources return ``None`` without calling the source resolver.
    ``read_only`` must be ``True`` and ``write_only`` must be ``False``.

    Args:
        transform: Transformation or name from ``IMGPROXYKIT['transforms']``.
            Omit to add no processing options.
        **kwargs: DRF field options. ``allow_null`` defaults to ``True``.

    """

    def __init__(
        self,
        *,
        transform: Transform | str | None = None,
        **kwargs: Any,
    ) -> None:
        """Configure the transformation and DRF field options."""
        # Remove these options before forwarding kwargs: their values are fixed
        # below, and passing them twice would raise TypeError.
        if kwargs.pop('read_only', True) is not True:
            raise ValueError('read_only must be True for ImgproxyURLField.')

        if kwargs.pop('write_only', False) is not False:
            raise ValueError('write_only must be False for ImgproxyURLField.')

        kwargs.setdefault('allow_null', True)
        super().__init__(read_only=True, write_only=False, **kwargs)
        self.transform = transform

    # Empty sources produce None, which URLField's return type excludes.
    @override
    def to_representation(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
        self,
        value: str | FieldFile | None,
    ) -> str | None:
        """Build an imgproxy URL, or return None for an empty source."""
        if not value:
            return None

        return imgproxy_url(value, self.transform)


class ImgproxyVariantsField(serializers.DictField):
    """
    Represent a source as a read-only dictionary of named imgproxy URLs.

    Use Django's ``IMGPROXYKIT`` settings and resolve the source once for
    all variants. Empty sources return ``None`` without calling the resolver.
    ``read_only`` must be ``True`` and ``write_only`` must be ``False``.
    ``child`` cannot be supplied; variant values always use a URL field.

    Args:
        variants: Transformation mapping or set name from
            ``IMGPROXYKIT['variants']``.
        **kwargs: DRF field options. ``allow_null`` defaults to ``True``.

    """

    def __init__(
        self,
        *,
        variants: Mapping[str, Transform] | str,
        **kwargs: Any,
    ) -> None:
        """Configure the variants and DRF field options."""
        # Remove these options before forwarding kwargs: their values are fixed
        # below, and passing them twice would raise TypeError.
        if kwargs.pop('read_only', True) is not True:
            raise ValueError(
                'read_only must be True for ImgproxyVariantsField.',
            )
        if kwargs.pop('write_only', False) is not False:
            raise ValueError(
                'write_only must be False for ImgproxyVariantsField.',
            )
        if 'child' in kwargs:
            raise TypeError(
                'child cannot be supplied for ImgproxyVariantsField.',
            )

        kwargs.setdefault('allow_null', True)
        super().__init__(  # pyright: ignore[reportUnknownMemberType]
            child=serializers.URLField(),
            read_only=True,
            write_only=False,
            **kwargs,
        )
        self.variants = variants

    # DictField's types exclude source strings, model files, and None output.
    @override
    def to_representation(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]  # ty: ignore[invalid-method-override]
        self,
        value: str | FieldFile | None,  # type: ignore[override]
    ) -> dict[str, str] | None:
        """Build named imgproxy URLs, or return None for an empty source."""
        if not value:
            return None

        return imgproxy_variants(value, self.variants)
