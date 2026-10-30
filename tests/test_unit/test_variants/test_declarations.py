from dataclasses import InitVar, dataclass, field, make_dataclass
from typing import Annotated, Any, Final

import pytest

from imgproxykit import Transform
from imgproxykit.variants import DataclassVariantsResolver

_SMALL: Final = Transform(width=320)
_Thumbnail = Annotated[str, _SMALL]


@dataclass
class _EmptyVariants:
    """Declare an empty result."""


@dataclass
class _NonInitVariants:
    """Declare a field that cannot receive a generated URL."""

    small: Annotated[str, _SMALL] = field(init=False)


def test_empty_declaration() -> None:
    """Allow declarations with no result fields."""
    assert DataclassVariantsResolver(model=_EmptyVariants)() == {}


def test_non_init_field() -> None:
    """Reject result fields that cannot be supplied to the constructor."""
    with pytest.raises(TypeError, match='init=False') as exc_info:
        DataclassVariantsResolver(model=_NonInitVariants)()

    assert "Field 'small'" in str(exc_info.value)
    assert '_NonInitVariants' in str(exc_info.value)


@pytest.mark.parametrize('annotation', [InitVar[str], InitVar])
def test_init_var(*, annotation: Any) -> None:
    """Identify typed and bare init-only fields instead of ignoring them."""
    model = make_dataclass(
        'InitOnlyVariants',
        [('token', annotation), ('small', _Thumbnail)],
    )

    with pytest.raises(TypeError, match='InitVar') as exc_info:
        DataclassVariantsResolver(model=model)()  # ty: ignore[invalid-argument-type]

    assert "Field 'token'" in str(exc_info.value)
    assert 'InitOnlyVariants' in str(exc_info.value)
