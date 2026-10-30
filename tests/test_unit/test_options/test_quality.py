from typing import Any

import pytest

from imgproxykit import Transform
from imgproxykit.options import Quality
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize('value', [0, 1, 50, 99, 100])
def test_quality_valid(path_serializer: PathSerializer, *, value: int) -> None:
    """Ensure that valid quality values serialize correctly."""
    option = Quality(value)
    expected = f'quality:{value}'
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )


@pytest.mark.parametrize('value', [0, 75, 100])
def test_quality_transform_valid(value: int) -> None:
    """Ensure that valid quality works with Transform kwargs."""
    transform = Transform(quality=value)
    assert transform.options == (Quality(value),)


@pytest.mark.parametrize(
    'invalid_value',
    [-10, -1, 101, 200, True, False, 85.5, '85'],
)
def test_quality_invalid(invalid_value: Any) -> None:
    """Ensure that invalid quality values raise ValueError."""
    with pytest.raises(
        ValueError,
        match='Quality must be an integer between 0 and 100',
    ):
        Quality(invalid_value)


@pytest.mark.parametrize('invalid_value', [-1, 101, True])
def test_quality_transform_invalid(invalid_value: Any) -> None:
    """Ensure that invalid quality in Transform kwargs raises ValueError."""
    with pytest.raises(
        ValueError,
        match='Quality must be an integer between 0 and 100',
    ):
        Transform(quality=invalid_value)  # type: ignore[arg-type]
