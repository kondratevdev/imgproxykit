from collections.abc import Callable

import pytest

from imgproxykit.options import Watermark
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Watermark(opacity=0), 'watermark:0'),
        (Watermark(opacity=0.5, scale=0), 'watermark:0.5::::0'),
        (
            Watermark(
                opacity=0.5,
                position='soea',
                offset_x=10,
                offset_y=20,
                scale=0.25,
            ),
            'watermark:0.5:soea:10:20:0.25',
        ),
    ],
)
def test_watermark(
    path_serializer: PathSerializer,
    *,
    option: Watermark,
    expected: str,
) -> None:
    """Ensure that watermark arguments retain their order and omitted slots."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )


@pytest.mark.parametrize(
    ('factory', 'position'),
    [
        (Watermark.center, 'ce'),
        (Watermark.top, 'no'),
        (Watermark.bottom, 'so'),
        (Watermark.left, 'we'),
        (Watermark.right, 'ea'),
        (Watermark.top_left, 'nowe'),
        (Watermark.top_right, 'noea'),
        (Watermark.bottom_left, 'sowe'),
        (Watermark.bottom_right, 'soea'),
    ],
)
@pytest.mark.parametrize(
    ('settings', 'suffix'),
    [
        ({}, ''),
        ({'offset_x': 0}, ':0'),
        ({'offset_y': 0}, '::0'),
        ({'scale': 0}, ':::0'),
        ({'offset_x': 0.25, 'offset_y': 20, 'scale': 0.5}, ':0.25:20:0.5'),
    ],
)
def test_anchor_factories(
    path_serializer: PathSerializer,
    *,
    factory: Callable[..., Watermark],
    position: str,
    settings: dict[str, float],
    suffix: str,
) -> None:
    """Preserve opacity, offsets, and scale for every readable anchor."""
    option = factory(opacity=0.5, **settings)

    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == f'watermark:0.5:{position}{suffix}'
    )


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Watermark.repeat(opacity=0), 'watermark:0:re'),
        (
            Watermark.repeat(opacity=0.5, spacing_x=0),
            'watermark:0.5:re:0',
        ),
        (
            Watermark.repeat(opacity=0.5, spacing_y=0, scale=0),
            'watermark:0.5:re::0:0',
        ),
        (
            Watermark.repeat(
                opacity=0.5,
                spacing_x=10,
                spacing_y=20,
                scale=0.25,
            ),
            'watermark:0.5:re:10:20:0.25',
        ),
    ],
)
def test_repeat_factory(
    path_serializer: PathSerializer,
    *,
    option: Watermark,
    expected: str,
) -> None:
    """Serialize tile spacing in the protocol's offset positions."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
