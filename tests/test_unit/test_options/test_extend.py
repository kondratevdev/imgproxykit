import pytest

from imgproxykit.options import Extend, Gravity
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Extend(value=False), 'extend:0'),
        (
            Extend(value=True, gravity=Gravity.focus(x=0.25, y=0.75)),
            'extend:1:fp:0.25:0.75',
        ),
        (
            Extend(value=True, gravity=Gravity.center(offset_y=0)),
            'extend:1:ce::0',
        ),
    ],
)
def test_extend(
    path_serializer: PathSerializer,
    *,
    option: Extend,
    expected: str,
) -> None:
    """Ensure that extension retains its flag, anchor, and offset positions."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
