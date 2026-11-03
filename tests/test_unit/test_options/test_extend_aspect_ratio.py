import pytest

from imgproxykit.options import ExtendAspectRatio, Gravity
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (ExtendAspectRatio(value=False), 'extend_aspect_ratio:0'),
        (
            ExtendAspectRatio(
                value=True,
                gravity=Gravity.focus(x=0.25, y=0.75),
            ),
            'extend_aspect_ratio:1:fp:0.25:0.75',
        ),
        (
            ExtendAspectRatio(value=True, gravity=Gravity.center(offset_y=0)),
            'extend_aspect_ratio:1:ce::0',
        ),
    ],
)
def test_extend_aspect_ratio(
    path_serializer: PathSerializer,
    *,
    option: ExtendAspectRatio,
    expected: str,
) -> None:
    """Ensure that aspect ratio extension retains its flag and gravity."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
