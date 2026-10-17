import pytest

from imgproxykit import options
from imgproxykit.internal.serialization import serialize_option
from tests.protocols import OptionFactory


@pytest.mark.parametrize(
    ('option_type', 'prefix'),
    [
        (options.AutoRotate, 'ar'),
        (options.EnforceThumbnail, 'eth'),
        (options.Enlarge, 'el'),
        (options.KeepCopyright, 'kcr'),
        (options.PreserveHDR, 'ph'),
        (options.Raw, 'raw'),
        (options.ReturnAttachment, 'att'),
        (options.StripColorProfile, 'scp'),
        (options.StripMetadata, 'sm'),
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
    assert (
        serialize_option(option_type(value=value)) == f'{prefix}:{int(value)}'
    )
