from dataclasses import dataclass, make_dataclass
from re import escape
from typing import Annotated, Any, Final

import pytest

from imgproxykit import Transform
from imgproxykit.variants import DataclassVariantsResolver

_SMALL: Final = Transform(width=320)
_LARGE: Final = Transform(width=1280)
_Thumbnail = Annotated[str, _SMALL]


@dataclass
class _AliasVariants:
    """Reference a module-level alias through a string annotation."""

    small: '_Thumbnail'


def test_alias_and_forward_reference() -> None:
    """Resolve a string annotation referring to a module-level type alias."""
    assert DataclassVariantsResolver(model=_AliasVariants)() == {
        'small': _SMALL
    }


@pytest.mark.parametrize(
    ('annotation', 'message'),
    [
        (str, 'must be annotated with `Annotated[str, Transform(...)]`'),
        (
            Annotated[int, _SMALL],
            'must be annotated with `Annotated[str, Transform(...)]`',
        ),
        (Annotated[str, 'description'], 'got 0'),
        (Annotated[str, _SMALL, _LARGE], 'got 2'),
        (Annotated[str, _SMALL, _SMALL], 'got 2'),
    ],
)
def test_invalid_annotation(*, annotation: Any, message: str) -> None:
    """Reject invalid result types and missing or repeated transformations."""
    model = make_dataclass('InvalidVariants', [('small', annotation)])

    with pytest.raises(TypeError, match=escape(message)) as exc_info:
        DataclassVariantsResolver(model=model)()  # ty: ignore[invalid-argument-type]

    assert "Field 'small'" in str(exc_info.value)
    assert 'InvalidVariants' in str(exc_info.value)


def test_unresolved_forward_reference() -> None:
    """Propagate unresolved application annotations without hiding the name."""
    model = make_dataclass(
        'UnresolvedVariants',
        [('small', 'MissingThumbnail')],
    )

    with pytest.raises(NameError, match='MissingThumbnail'):
        DataclassVariantsResolver(model=model)()  # ty: ignore[invalid-argument-type]
