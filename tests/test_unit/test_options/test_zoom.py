import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Zoom


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Zoom(factor_x=1.5), 'zoom:1.5'),
        (Zoom(factor_x=1.5, factor_y=2.5), 'zoom:1.5:2.5'),
    ],
)
def test_zoom(*, option: Zoom, expected: str) -> None:
    """Ensure that zoom supports uniform and independent axis factors."""
    assert serialize_option(option) == expected
