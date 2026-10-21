import pytest

from imgproxykit.options import Gravity
from imgproxykit.serialization import PathSerializer


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
    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == expected
    )
