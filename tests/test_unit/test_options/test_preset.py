import pytest

from imgproxykit.options import Preset
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Preset(), 'preset'),
        (Preset('thumbnail'), 'preset:thumbnail'),
        (
            Preset('thumbnail', 'watermarked'),
            'preset:thumbnail:watermarked',
        ),
        # Names keep the order they were supplied in.
        (
            Preset('watermarked', 'thumbnail'),
            'preset:watermarked:thumbnail',
        ),
    ],
)
def test_preset(
    path_serializer: PathSerializer,
    *,
    option: Preset,
    expected: str,
) -> None:
    """Ensure that preset names are positional and keep their order."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )


def test_preset_keeps_dataclass_equality() -> None:
    """Ensure that positional construction keeps dataclass equality."""
    assert Preset('thumbnail') == Preset('thumbnail')
    assert Preset('thumbnail', 'watermarked') == Preset(
        'thumbnail',
        'watermarked',
    )
    assert Preset('thumbnail') != Preset('watermarked')
