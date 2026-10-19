from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Gravity

_OFFSET_X: Final = 0.25
_OFFSET_Y: Final = 0.75


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Gravity(position='ce'), 'gravity:ce'),
        (
            Gravity(
                position='fp',
                offset_x=_OFFSET_X,
                offset_y=_OFFSET_Y,
            ),
            'gravity:fp:0.25:0.75',
        ),
        (Gravity(position='no', offset_y=0), 'gravity:no::0'),
    ],
)
def test_gravity(*, option: Gravity, expected: str) -> None:
    """Ensure that gravity retains its anchor and optional offset positions."""
    assert serialize_option(option) == expected
