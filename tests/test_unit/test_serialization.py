from typing import Final

import pytest

from imgproxykit import Transform
from imgproxykit.options import Format, Preset, Quality, Resize
from imgproxykit.serialization import PathSerializer
from imgproxykit.types import Argument

_SOURCE: Final = 'https://example.com/photo.jpg'


@pytest.mark.parametrize(
    ('source', 'expected'),
    [
        # An HTTPS source is encoded without Base64 padding.
        (_SOURCE, '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'),
        # Unicode and query parameters are preserved.
        (
            's3://bucket/café.jpg?version=1',
            '/czM6Ly9idWNrZXQvY2Fmw6kuanBnP3ZlcnNpb249MQ',
        ),
    ],
)
def test_source_path(*, source: str, expected: str) -> None:
    """Ensure that sources are encoded unchanged without Base64 padding."""
    assert PathSerializer()(source) == expected


@pytest.mark.parametrize(
    ('transform', 'expected'),
    [
        # Processing options retain their order.
        (
            Transform(
                Quality(85),
                Resize(width=300, height=200, mode='fill'),
                Format('webp'),
            ),
            '/quality:85/resize:fill:300:200/format:webp/',
        ),
        # Names within a preset retain their order.
        (
            Transform(Preset('thumbnail', 'watermarked')),
            '/preset:thumbnail:watermarked/',
        ),
        # Presets retain their positions around overrides.
        (
            Transform(
                Preset('thumbnail'),
                Quality(85),
                Preset('watermarked'),
            ),
            '/preset:thumbnail/quality:85/preset:watermarked/',
        ),
        # Repeated formats retain their positions around presets.
        (
            Transform(
                Format('webp'),
                Preset('thumbnail'),
                Format('avif'),
            ),
            '/format:webp/preset:thumbnail/format:avif/',
        ),
        # An empty transform adds no processing segments.
        (Transform(), '/'),
    ],
)
def test_transform_path(*, transform: Transform, expected: str) -> None:
    """Ensure that transform options retain their order before the source."""
    assert PathSerializer()(_SOURCE, transform=transform) == (
        f'{expected}aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


@pytest.mark.parametrize(
    ('arguments', 'expected'),
    [
        # No arguments produce only the option name.
        ((), 'resize'),
        # All trailing None values are omitted.
        ((None, None), 'resize'),
        # Trailing None values after an explicit value are omitted.
        (('fill', None, None), 'resize:fill'),
        # Leading None values retain their positions.
        ((None, 300, None), 'resize::300'),
        # Internal None values retain their positions.
        ((300, None, 200), 'resize:300::200'),
        # Consecutive internal None values retain their positions.
        (('fill', None, None, True), 'resize:fill:::1'),
        # Booleans are serialized as integers.
        ((True, False), 'resize:1:0'),
        # Floats preserve their string representation, including zero.
        ((0.0, 1.5), 'resize:0.0:1.5'),  # noqa: WPS358
        # An explicit empty string is preserved.
        (('', None), 'resize:'),
        # False is preserved before trailing None values.
        ((False, None), 'resize:0'),
        # Integer zero is preserved before trailing None values.
        ((0, None), 'resize:0'),
        # Unicode arguments are preserved.
        (('café',), 'resize:café'),
    ],
)
def test_serialize_segment(
    *,
    arguments: tuple[Argument, ...],
    expected: str,
) -> None:
    """Ensure that arguments retain their positions and explicit values."""
    assert PathSerializer()._serialize_segment('resize', arguments) == expected


def test_custom_arguments_separator() -> None:
    """Ensure that custom separators preserve omitted argument positions."""
    serializer = PathSerializer(arguments_separator=',')
    transform = Transform(Resize(width=300), format='webp')
    assert serializer(_SOURCE, transform=transform) == (
        '/resize,,300/format,webp/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )
