from typing import Final

import pytest

from imgproxykit.options import Trim
from imgproxykit.serialization import PathSerializer

_THRESHOLD: Final = 10
_BACKGROUND_COLOR: Final = 'ffffff'
_TRANSPARENCY_KEY: Final = 'FF00FF'


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        # Zero tolerance is preserved without a color or symmetry flags.
        (Trim(threshold=0), 'trim:0'),
        # Explicit background color and both symmetry flags retain their order.
        (
            Trim(
                threshold=_THRESHOLD,
                color=_BACKGROUND_COLOR,
                equal_hor=True,
                equal_ver=False,
            ),
            f'trim:{_THRESHOLD}:{_BACKGROUND_COLOR}:1:0',
        ),
        # Omitted color and horizontal symmetry retain their positions.
        (Trim(threshold=_THRESHOLD, equal_ver=False), f'trim:{_THRESHOLD}:::0'),
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


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        # Zero tolerance is preserved with the transparency key.
        (Trim.transparent(threshold=0), f'trim:0:{_TRANSPARENCY_KEY}'),
        # Fractional tolerance is preserved without symmetry flags.
        (Trim.transparent(threshold=0.5), f'trim:0.5:{_TRANSPARENCY_KEY}'),
        # Both symmetry flags retain their explicit boolean values.
        (
            Trim.transparent(
                threshold=_THRESHOLD,
                equal_hor=True,
                equal_ver=False,
            ),
            f'trim:{_THRESHOLD}:{_TRANSPARENCY_KEY}:1:0',
        ),
        # An omitted horizontal flag retains its position before vertical.
        (
            Trim.transparent(threshold=_THRESHOLD, equal_ver=True),
            f'trim:{_THRESHOLD}:{_TRANSPARENCY_KEY}::1',
        ),
        # An explicit horizontal False is retained without a vertical flag.
        (
            Trim.transparent(threshold=_THRESHOLD, equal_hor=False),
            f'trim:{_THRESHOLD}:{_TRANSPARENCY_KEY}:0',
        ),
    ],
)
def test_trim_transparent(
    path_serializer: PathSerializer,
    *,
    option: Trim,
    expected: str,
) -> None:
    """Ensure that transparent trimming retains its key color and flags."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
