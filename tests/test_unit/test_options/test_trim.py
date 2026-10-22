import pytest

from imgproxykit.options import Trim
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Trim(threshold=0), 'trim:0'),
        (
            Trim(
                threshold=10,
                color='ffffff',
                equal_hor=True,
                equal_ver=False,
            ),
            'trim:10:ffffff:1:0',
        ),
        (Trim(threshold=10, equal_ver=False), 'trim:10:::0'),
    ],
)
def test_trim(
    path_serializer: PathSerializer,
    *,
    option: Trim,
    expected: str,
) -> None:
    """Ensure that trim retains its threshold, color, and symmetry flags."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
