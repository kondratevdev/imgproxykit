from typing import Any

import pytest

from imgproxykit import Transform
from imgproxykit.options import Rotate
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize('angle', [0, 90, 180, 270, 360, -90, -180])
def test_rotate_valid(path_serializer: PathSerializer, *, angle: int) -> None:
    """Ensure that valid rotation angles serialize correctly."""
    option = Rotate(angle)
    expected = f'rotate:{angle}'
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )


@pytest.mark.parametrize('angle', [0, 90, 180, 270])
def test_rotate_transform_valid(angle: int) -> None:
    """Ensure that valid rotation angle works with Transform kwargs."""
    transform = Transform(rotate=angle)
    assert transform.options == (Rotate(angle),)


@pytest.mark.parametrize(
    'invalid_angle',
    [1, 45, 89, 91, 100, -45, True, False, 90.0, '90'],
)
def test_rotate_invalid(invalid_angle: Any) -> None:
    """Ensure that invalid rotation angles raise ValueError."""
    with pytest.raises(
        ValueError,
        match='Angle must be an integer multiple of 90',
    ):
        Rotate(invalid_angle)


@pytest.mark.parametrize('invalid_angle', [45, 100, True])
def test_rotate_transform_invalid(invalid_angle: Any) -> None:
    """Ensure that invalid rotation in Transform kwargs raises ValueError."""
    with pytest.raises(
        ValueError,
        match='Angle must be an integer multiple of 90',
    ):
        Transform(rotate=invalid_angle)  # type: ignore[arg-type]
