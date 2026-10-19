from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Watermark

_RIGHT: Final = 20
_OFFSET_X: Final = 0.25


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Watermark(opacity=0), 'watermark:0'),
        (
            Watermark(
                opacity=0.5,
                position='soea',
                offset_x=10,
                offset_y=_RIGHT,
                scale=_OFFSET_X,
            ),
            'watermark:0.5:soea:10:20:0.25',
        ),
        (Watermark(opacity=0.5, scale=0), 'watermark:0.5::::0'),
    ],
)
def test_watermark(*, option: Watermark, expected: str) -> None:
    """Ensure that watermark arguments retain their order and omitted slots."""
    assert serialize_option(option) == expected
