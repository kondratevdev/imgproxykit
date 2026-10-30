import pytest

from imgproxykit import Transform
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


@pytest.mark.parametrize(
    'preset_name',
    [
        'thumbnail',
        'thumb.v1',
        'thumb_v1-x~y',
        "a!$&'()*+,;=:@",
    ],
)
def test_preset_accepts_url_safe_names(preset_name: str) -> None:
    """Ensure that names a URL path carries literally are accepted."""
    assert Preset(preset_name).names == (preset_name,)


@pytest.mark.parametrize(
    'preset_name',
    [
        '',
        'thumb#v1',
        'thumb?v1',
        'thumb/v1',
        'thumb%23v1',
        'thumb v1',
        'café',
        'thumb\nv1',
    ],
)
def test_preset_rejects_unsupported_names(preset_name: str) -> None:
    """Ensure that names changing the URL structure are rejected."""
    with pytest.raises(ValueError, match='Preset names must'):
        Preset('thumbnail', preset_name)


@pytest.mark.parametrize(
    ('arguments_separator', 'preset_name'),
    [
        (':', 'thumb:v1'),
        (',', 'thumb,v1'),
        ('.', 'thumb.v1'),
    ],
)
def test_preset_rejects_arguments_separator(
    *,
    arguments_separator: str,
    preset_name: str,
) -> None:
    """Ensure that a name containing the separator is not split in two."""
    serializer = PathSerializer(
        arguments_separator=arguments_separator,
        short_option_name=False,
    )

    with pytest.raises(ValueError, match='arguments separator'):
        serializer(
            'local:///source.png',
            transform=Transform(Preset(preset_name)),
        )


def test_preset_allows_other_separator() -> None:
    """Ensure that only the configured separator is rejected."""
    serializer = PathSerializer(
        arguments_separator=',',
        short_option_name=False,
    )

    path = serializer(
        'local:///source.png',
        transform=Transform(Preset('a:b')),
    )

    assert path.startswith('/preset,a:b/')
