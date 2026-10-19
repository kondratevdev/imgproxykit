from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Size

_WIDTH: Final = 300
_HEIGHT: Final = 200


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Size(), 'size'),
        (
            Size(width=_WIDTH, height=_HEIGHT, enlarge=False, extend=True),
            'size:300:200:0:1',
        ),
        (Size(height=_HEIGHT), 'size::200'),
        (Size(extend=False), 'size::::0'),
    ],
)
def test_size(*, option: Size, expected: str) -> None:
    """Ensure that size arguments retain dimension and boolean positions."""
    assert serialize_option(option) == expected
