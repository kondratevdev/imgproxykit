from dataclasses import dataclass
from typing import Annotated, ClassVar, Final

from imgproxykit import Transform
from imgproxykit.variants import DataclassVariantsResolver

_SMALL: Final = Transform(width=320)
_LARGE: Final = Transform(width=1280)


@dataclass(frozen=True, slots=True, kw_only=True)
class _BaseVariants:
    """Declare an inherited field and a non-field class attribute."""

    small: Annotated[str, _SMALL]
    label: ClassVar[str] = 'images'


@dataclass(frozen=True, slots=True, kw_only=True)
class _InheritedVariants(_BaseVariants):
    """Extend the declaration with unrelated annotation metadata."""

    large: Annotated[str, 'description', _LARGE, 42]


@dataclass(frozen=True, slots=True, kw_only=True)
class _OverriddenVariants(_BaseVariants):
    """Replace the transformation of an inherited result field."""

    small: Annotated[str, _LARGE]


def test_resolve_fields() -> None:
    """Preserve field order and transformations, ignoring other metadata."""
    transforms = DataclassVariantsResolver(model=_InheritedVariants)()

    assert list(transforms) == ['small', 'large']
    assert transforms == {'small': _SMALL, 'large': _LARGE}


def test_override_inherited_field() -> None:
    """Use the subclass annotation when an inherited field is overridden."""
    transforms = DataclassVariantsResolver(model=_OverriddenVariants)()

    assert transforms == {'small': _LARGE}


def test_fresh_mapping() -> None:
    """Return independent mappings when resolving the same declaration."""
    resolver = DataclassVariantsResolver(model=_BaseVariants)
    first = resolver()
    second = resolver()
    first.clear()

    assert second == {'small': _SMALL}
