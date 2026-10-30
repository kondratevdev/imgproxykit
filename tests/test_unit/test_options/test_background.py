import pytest

from imgproxykit.options import Background
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Background(), 'background'),
        (Background(color='ff0080'), 'background:ff0080'),
        (Background(color=(0, 128, 255)), 'background:0:128:255'),
        (Background.rgb(red=0, green=128, blue=255), 'background:0:128:255'),
        (Background.hex('ff0080'), 'background:ff0080'),
        (Background.disabled(), 'background'),
    ],
)
def test_background(
    path_serializer: PathSerializer,
    *,
    option: Background,
    expected: str,
) -> None:
    """Ensure that backgrounds accept hex colors, RGB tuples, and omission."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
