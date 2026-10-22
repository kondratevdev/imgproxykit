import pytest

from imgproxykit.options import Watermark
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Watermark(opacity=0), 'watermark:0'),
        (Watermark(opacity=0.5, scale=0), 'watermark:0.5::::0'),
        (
            Watermark(
                opacity=0.5,
                position='soea',
                offset_x=10,
                offset_y=20,
                scale=0.25,
            ),
            'watermark:0.5:soea:10:20:0.25',
        ),
    ],
)
def test_watermark(
    path_serializer: PathSerializer,
    *,
    option: Watermark,
    expected: str,
) -> None:
    """Ensure that watermark arguments retain their order and omitted slots."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
