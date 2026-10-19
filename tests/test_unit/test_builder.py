from typing import Final

import pytest
from inline_snapshot import snapshot

from imgproxykit import Transform
from imgproxykit.builder import PathBuilder
from imgproxykit.options import Format, Preset, Quality, Resize

_SOURCE: Final = 'https://example.com/photo.jpg'
_WIDTH: Final = 300
_HEIGHT: Final = 200
_QUALITY: Final = 85


@pytest.mark.parametrize(
    ('source', 'expected'),
    [
        (_SOURCE, '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'),
        (
            's3://bucket/café.jpg?version=1',
            '/czM6Ly9idWNrZXQvY2Fmw6kuanBnP3ZlcnNpb249MQ',
        ),
    ],
)
def test_source_path(*, source: str, expected: str) -> None:
    """Ensure that sources are encoded unchanged without Base64 padding."""
    assert PathBuilder()(source) == expected


def test_transform_path() -> None:
    """Ensure that transform options retain their order before the source."""
    transform = Transform(
        Quality(_QUALITY),
        Resize(width=_WIDTH, height=_HEIGHT, mode='fill'),
        Format('webp'),
    )

    assert PathBuilder()(_SOURCE, transform=transform) == snapshot(
        '/q:85/rs:fill:300:200/f:webp/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


@pytest.mark.parametrize(
    ('transform', 'expected'),
    [
        (Transform(), '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'),
        (
            Transform(Format('webp')),
            '/f:webp/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        ),
        (
            Transform(Quality(_QUALITY)),
            '/q:85/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        ),
    ],
)
def test_partial_transform_path(*, transform: Transform, expected: str) -> None:
    """Ensure that transform options and format can be omitted independently."""
    assert PathBuilder()(_SOURCE, transform=transform) == expected


def test_empty_presets_path() -> None:
    """Ensure that explicit empty presets retain the preset segment."""
    assert PathBuilder()(
        _SOURCE, transform=Transform(Preset(names=()))
    ) == snapshot(
        '/pr/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_presets_path() -> None:
    """Ensure that presets retain their order and accept an output format."""
    assert PathBuilder()(
        _SOURCE,
        transform=Transform(Preset(names=('thumbnail', 'watermarked'))),
    ) == snapshot(
        '/pr:thumbnail:watermarked/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )
    assert PathBuilder()(
        _SOURCE,
        transform=Transform(
            Preset(names=('thumbnail',)),
            Format('avif'),
        ),
    ) == snapshot(
        '/pr:thumbnail/f:avif/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


def test_interleaved_presets() -> None:
    """Ensure that preset references preserve positions around overrides."""
    transform = Transform(
        Preset(names=('thumbnail',)),
        Quality(_QUALITY),
        Preset(names=('watermarked',)),
    )
    assert PathBuilder()(_SOURCE, transform=transform) == (
        '/pr:thumbnail/q:85/pr:watermarked/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


def test_interleaved_formats() -> None:
    """Ensure that format options preserve their order around presets."""
    transform = Transform(
        Format('webp'),
        Preset(names=('thumbnail',)),
        Format('avif'),
    )
    assert PathBuilder()(_SOURCE, transform=transform) == (
        '/f:webp/pr:thumbnail/f:avif/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )
