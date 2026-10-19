from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Padding

_RIGHT: Final = 20
_BOTTOM: Final = 30
_LEFT: Final = 40


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Padding(), 'padding'),
        (
            Padding(
                top=10,
                right=_RIGHT,
                bottom=_BOTTOM,
                left=_LEFT,
            ),
            'padding:10:20:30:40',
        ),
        (Padding(left=0), 'padding::::0'),
    ],
)
def test_padding(*, option: Padding, expected: str) -> None:
    """Ensure that padding uses CSS side order and retains omitted sides."""
    assert serialize_option(option) == expected
