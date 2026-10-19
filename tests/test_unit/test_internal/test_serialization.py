from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_segment
from imgproxykit.types import EMPTY, Argument

_WIDTH: Final = 300
_HEIGHT: Final = 200


@pytest.mark.parametrize(
    ('arguments', 'expected'),
    [
        ((), 'resize'),
        ((EMPTY,), 'resize'),
        ((EMPTY, EMPTY), 'resize'),
        (('fill', EMPTY, EMPTY), 'resize:fill'),
        ((EMPTY, _WIDTH, EMPTY), 'resize::300'),
        ((_WIDTH, EMPTY, _HEIGHT), 'resize:300::200'),
        (('fill', EMPTY, EMPTY, True), 'resize:fill:::1'),
        ((True, False), 'resize:1:0'),
        ((0,), 'resize:0'),
        ((0.0, 1.5), 'resize:0.0:1.5'),  # noqa: WPS358
        (('',), 'resize:'),
        (('', EMPTY), 'resize:'),
        ((False, EMPTY), 'resize:0'),
        ((0, EMPTY), 'resize:0'),
        (('café',), 'resize:café'),
    ],
)
def test_serialize_segment(
    *,
    arguments: tuple[Argument, ...],
    expected: str,
) -> None:
    """Ensure that arguments retain their positions and explicit values."""
    assert serialize_segment('resize', arguments) == expected
