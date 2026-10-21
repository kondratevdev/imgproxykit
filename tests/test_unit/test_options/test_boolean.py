import pytest

from imgproxykit import options
from imgproxykit.serialization import PathSerializer
from tests.infra import OptionFactory


@pytest.mark.parametrize(
    ('option_type', 'prefix'),
    [
        (options.AutoRotate, 'auto_rotate'),
        (options.EnforceThumbnail, 'enforce_thumbnail'),
        (options.Enlarge, 'enlarge'),
        (options.KeepCopyright, 'keep_copyright'),
        (options.PreserveHDR, 'preserve_hdr'),
        (options.Raw, 'raw'),
        (options.ReturnAttachment, 'return_attachment'),
        (options.StripColorProfile, 'strip_color_profile'),
        (options.StripMetadata, 'strip_metadata'),
    ],
)
@pytest.mark.parametrize('value', [True, False])
def test_boolean_options(
    *,
    option_type: OptionFactory[bool],
    prefix: str,
    value: bool,
) -> None:
    """Ensure that boolean options serialize enabled and disabled values."""
    option = option_type(value=value)

    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == f'{prefix}:{int(value)}'
    )
