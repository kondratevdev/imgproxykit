import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Flip


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Flip(), 'flip'),
        (Flip(horizontal=True, vertical=False), 'flip:1:0'),
        (Flip(vertical=False), 'flip::0'),
    ],
)
def test_flip(*, option: Flip, expected: str) -> None:
    """Ensure that flip axes retain positions and explicit false values."""
    assert serialize_option(option) == expected
