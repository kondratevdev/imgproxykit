import math

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


_INVALID_FACTORS = (
    0,
    -1,
    -0.5,
    math.nan,
    math.inf,
    -math.inf,
)


@pytest.mark.parametrize('factor', [0.5, 1, 2.5])
def test_zoom_valid_factors(*, factor: float) -> None:
    """Ensure that fractional and whole positive factors are accepted."""
    assert Zoom(factor_x=factor, factor_y=factor).arguments == (factor, factor)


@pytest.mark.parametrize('factor', _INVALID_FACTORS)
def test_zoom_invalid_factor_x(*, factor: float) -> None:
    """Ensure that a horizontal factor must be finite and positive."""
    with pytest.raises(ValueError, match='factor_x'):
        Zoom(factor_x=factor)


@pytest.mark.parametrize('factor', _INVALID_FACTORS)
def test_zoom_invalid_factor_y(*, factor: float) -> None:
    """Ensure that a vertical factor must be finite and positive."""
    with pytest.raises(ValueError, match='factor_y'):
        Zoom(factor_x=1, factor_y=factor)
