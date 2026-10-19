import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Extend


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Extend(value=False), 'extend:0'),
        (
            Extend(
                value=True,
                gravity='fp',
                offset_x=0.25,
                offset_y=0.75,
            ),
            'extend:1:fp:0.25:0.75',
        ),
        (Extend(value=True, offset_y=0), 'extend:1:::0'),
    ],
)
def test_extend(*, option: Extend, expected: str) -> None:
    """Ensure that extension retains its flag, anchor, and offset positions."""
    assert serialize_option(option) == expected
