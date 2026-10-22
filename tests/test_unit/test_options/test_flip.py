import pytest

from imgproxykit.options import Flip
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Flip(), 'flip'),
        (Flip(horizontal=True, vertical=False), 'flip:1:0'),
        (Flip(vertical=False), 'flip::0'),
    ],
)
def test_flip(
    path_serializer: PathSerializer,
    *,
    option: Flip,
    expected: str,
) -> None:
    """Ensure that flip axes retain positions and explicit false values."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
