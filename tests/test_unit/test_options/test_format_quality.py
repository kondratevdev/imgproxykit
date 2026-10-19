import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import FormatQuality


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (FormatQuality(qualities=()), 'format_quality'),
        (FormatQuality(qualities=(('webp', 0),)), 'format_quality:webp:0'),
        (
            FormatQuality(qualities=(('webp', 80), ('jpg', 90))),
            'format_quality:webp:80:jpg:90',
        ),
    ],
)
def test_format_quality(*, option: FormatQuality, expected: str) -> None:
    """Ensure that format quality pairs retain their order when flattened."""
    assert serialize_option(option) == expected
