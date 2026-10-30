from collections.abc import Callable

import pytest

from imgproxykit.options import Gravity
from imgproxykit.serialization import PathSerializer
from imgproxykit.types import Position


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Gravity(position='ce'), 'gravity:ce'),
        (
            Gravity(
                position='fp',
                offset_x=0.25,
                offset_y=0.75,
            ),
            'gravity:fp:0.25:0.75',
        ),
        (Gravity(position='no', offset_y=0), 'gravity:no::0'),
    ],
)
def test_gravity(
    path_serializer: PathSerializer,
    *,
    option: Gravity,
    expected: str,
) -> None:
    """Ensure that gravity retains its anchor and optional offset positions."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )


@pytest.mark.parametrize(
    ('factory', 'position'),
    [
        (Gravity.center, 'ce'),
        (Gravity.top, 'no'),
        (Gravity.bottom, 'so'),
        (Gravity.left, 'we'),
        (Gravity.right, 'ea'),
        (Gravity.top_left, 'nowe'),
        (Gravity.top_right, 'noea'),
        (Gravity.bottom_left, 'sowe'),
        (Gravity.bottom_right, 'soea'),
    ],
)
@pytest.mark.parametrize(
    ('offsets', 'suffix'),
    [
        ({}, ''),
        ({'offset_x': 0}, ':0'),
        ({'offset_y': 0}, '::0'),
        ({'offset_x': 0.25, 'offset_y': 20}, ':0.25:20'),
    ],
)
def test_anchor_factories(
    path_serializer: PathSerializer,
    *,
    factory: Callable[..., Gravity],
    position: Position,
    offsets: dict[str, float],
    suffix: str,
) -> None:
    """Serialize each readable anchor with omitted and explicit offsets."""
    option = factory(**offsets)

    assert option == Gravity(position=position, **offsets)
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == f'gravity:{position}{suffix}'
    )


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Gravity.smart(), 'gravity:sm'),
        (Gravity.focus(x=0.25, y=0.75), 'gravity:fp:0.25:0.75'),
        (Gravity.focus(x=0, y=1), 'gravity:fp:0:1'),
        (Gravity.focus(x=1, y=0), 'gravity:fp:1:0'),
    ],
)
def test_special_factories(
    path_serializer: PathSerializer,
    *,
    option: Gravity,
    expected: str,
) -> None:
    """Serialize smart gravity and focus coordinates, including endpoints."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
