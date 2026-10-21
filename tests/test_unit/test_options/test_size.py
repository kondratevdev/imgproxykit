import pytest

from imgproxykit.options import Size
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Size(), 'size'),
        (
            Size(
                width=300,
                height=200,
                enlarge=False,
                extend=True,
            ),
            'size:300:200:0:1',
        ),
        (Size(height=200), 'size::200'),
        (Size(extend=False), 'size::::0'),
    ],
)
def test_size(*, option: Size, expected: str) -> None:
    """Ensure that size arguments retain dimension and boolean positions."""
    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == expected
    )
