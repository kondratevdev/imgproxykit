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


def test_preset_unicode_supported(path_serializer: PathSerializer) -> None:
    """Ensure Unicode preset names are supported and serialized correctly."""
    preset = Preset('миниатюра', 'café')
    assert (
        path_serializer._serialize_segment(preset.name, preset.arguments)
        == 'preset:миниатюра:café'
    )


def test_preset_empty_name_raises_value_error() -> None:
    """Ensure empty string preset name raises ValueError."""
    with pytest.raises(ValueError, match=r'Preset name cannot be empty\.'):
        Preset('')


@pytest.mark.parametrize('reserved', ['#', '?', '/', ':'])
def test_preset_reserved_characters_raise_value_error(reserved: str) -> None:
    """Ensure reserved characters in preset name raise ValueError."""
    with pytest.raises(
        ValueError,
        match=r'Preset name .* contains reserved character .*',
    ):
        Preset(f'thumb{reserved}v1')


def test_custom_arguments_separator_conflict_raises_value_error() -> None:
    """Ensure argument containing configured separator raises ValueError."""
    serializer = PathSerializer(
        arguments_separator='@',
        short_option_name=False,
    )
    expected_error = (
        r"Option argument 'thumb@v1' contains the arguments separator '@'\."
    )
    with pytest.raises(ValueError, match=expected_error):
        serializer._serialize_segment('preset', ('thumb@v1',))
