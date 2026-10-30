import pytest

from imgproxykit import Transform
from imgproxykit.options import DPR


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
def test_dpr_invalid_value(invalid_factor: float) -> None:
    """Ensure that invalid DPR factor raises a ValueError."""
    with pytest.raises(
        ValueError,
        match='DPR factor must be greater than zero',
    ):
        DPR(invalid_factor)


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
def test_transform_dpr_invalid_keyword(invalid_factor: float) -> None:
    """Ensure that Transform(dpr=...) behaves consistently on invalid values."""
    with pytest.raises(
        ValueError,
        match='DPR factor must be greater than zero',
    ):
        Transform(dpr=invalid_factor)


@pytest.mark.parametrize('valid_factor', [0.25, 0.5, 1, 1.5, 2, 3.0])
def test_dpr_valid_value(valid_factor: float) -> None:
    """Ensure that finite factors greater than zero are accepted."""
    option = DPR(valid_factor)
    assert option.value == valid_factor

    transform = Transform(dpr=valid_factor)
    assert transform.options == (option,)
