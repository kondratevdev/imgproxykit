import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import ExtendAspectRatio


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (ExtendAspectRatio(value=False), 'extend_aspect_ratio:0'),
        (
            ExtendAspectRatio(
                value=True,
                gravity='fp',
                offset_x=0.25,
                offset_y=0.75,
            ),
            'extend_aspect_ratio:1:fp:0.25:0.75',
        ),
        (
            ExtendAspectRatio(value=True, offset_y=0),
            'extend_aspect_ratio:1:::0',
        ),
    ],
)
def test_extend_aspect_ratio(
    *, option: ExtendAspectRatio, expected: str
) -> None:
    """Ensure that aspect ratio extension retains its flag and gravity."""
    assert serialize_option(option) == expected
