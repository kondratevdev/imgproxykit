from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Crop

_HEIGHT: Final = 0.75
_OFFSET_X: Final = 0.25
_OFFSET_Y: Final = 0.125


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Crop(), 'crop'),
        (
            Crop(
                width=0.5,
                height=_HEIGHT,
                gravity='fp',
                offset_x=_OFFSET_X,
                offset_y=_OFFSET_Y,
            ),
            'crop:0.5:0.75:fp:0.25:0.125',
        ),
        (Crop(offset_y=0), 'crop:::::0'),
    ],
)
def test_crop(*, option: Crop, expected: str) -> None:
    """Ensure that crop dimensions and focus offsets retain their positions."""
    assert serialize_option(option) == expected
