import pytest

from imgproxykit.options import Extend
from imgproxykit.serialization import PathSerializer


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
    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == expected
    )
