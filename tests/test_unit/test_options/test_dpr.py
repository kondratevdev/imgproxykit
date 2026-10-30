import math

import pytest

from imgproxykit import Transform
from imgproxykit.options import DPR

_INVALID_FACTORS = (
    0,
    -1,
    -0.5,
    math.nan,
    math.inf,
    -math.inf,
)


@pytest.mark.parametrize('factor', [0.5, 1, 2.5])
def test_dpr_valid_factors(*, factor: float) -> None:
    """Ensure that fractional and whole positive factors are accepted."""
    assert DPR(factor).arguments == (factor,)
    assert Transform(dpr=factor).options == (DPR(factor),)


@pytest.mark.parametrize('factor', _INVALID_FACTORS)
def test_dpr_invalid_factor(*, factor: float) -> None:
    """Ensure that the multiplier must be finite and positive."""
    with pytest.raises(ValueError, match='DPR'):
        DPR(factor)


@pytest.mark.parametrize('factor', _INVALID_FACTORS)
def test_transform_invalid_dpr(*, factor: float) -> None:
    """Ensure that the keyword argument is validated the same way."""
    with pytest.raises(ValueError, match='DPR'):
        Transform(dpr=factor)
