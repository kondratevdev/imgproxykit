from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Zoom

_FACTOR: Final = 1.5
_FACTOR_Y: Final = 2.5


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Zoom(factor_x=_FACTOR), 'zoom:1.5'),
        (Zoom(factor_x=_FACTOR, factor_y=_FACTOR_Y), 'zoom:1.5:2.5'),
    ],
)
def test_zoom(*, option: Zoom, expected: str) -> None:
    """Ensure that zoom supports uniform and independent axis factors."""
    assert serialize_option(option) == expected
