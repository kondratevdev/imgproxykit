import pytest

from imgproxykit.options import Zoom
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Zoom(factor_x=1.5), 'zoom:1.5'),
        (Zoom(factor_x=1.5, factor_y=2.5), 'zoom:1.5:2.5'),
    ],
)
def test_zoom(
    path_serializer: PathSerializer,
    *,
    option: Zoom,
    expected: str,
) -> None:
    """Ensure that zoom supports uniform and independent axis factors."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )


@pytest.mark.parametrize(
    'invalid_factor',
    [
        0,
        0.0,
        -1,
        -0.5,
        float('nan'),
        float('inf'),
        float('-inf'),
    ],
)
def test_zoom_invalid_factor_x(invalid_factor: float) -> None:
    """Ensure that invalid factor_x raises a ValueError."""
    with pytest.raises(
        ValueError,
        match='Zoom factor_x must be greater than zero',
    ):
        Zoom(factor_x=invalid_factor)


@pytest.mark.parametrize(
    'invalid_factor',
    [
        0,
        0.0,
        -1,
        -0.5,
        float('nan'),
        float('inf'),
        float('-inf'),
    ],
)
def test_zoom_invalid_factor_y(invalid_factor: float) -> None:
    """Ensure that invalid factor_y raises a ValueError."""
    with pytest.raises(
        ValueError,
        match='Zoom factor_y must be greater than zero',
    ):
        Zoom(factor_x=1.5, factor_y=invalid_factor)
