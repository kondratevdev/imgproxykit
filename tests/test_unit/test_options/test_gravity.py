import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Gravity


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Gravity(position='ce'), 'gravity:ce'),
        (
            Gravity(
                position='fp',
                offset_x=0.25,
                offset_y=0.75,
            ),
            'gravity:fp:0.25:0.75',
        ),
        (Gravity(position='no', offset_y=0), 'gravity:no::0'),
    ],
)
def test_gravity(*, option: Gravity, expected: str) -> None:
    """Ensure that gravity retains its anchor and optional offset positions."""
    assert serialize_option(option) == expected
