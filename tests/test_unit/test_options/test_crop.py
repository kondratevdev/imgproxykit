import pytest

from imgproxykit.options import Crop
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Crop(), 'crop'),
        (
            Crop(
                width=0.5,
                height=0.75,
                gravity='fp',
                offset_x=0.25,
                offset_y=0.125,
            ),
            'crop:0.5:0.75:fp:0.25:0.125',
        ),
        (Crop(offset_y=0), 'crop:::::0'),
    ],
)
def test_crop(
    path_serializer: PathSerializer,
    *,
    option: Crop,
    expected: str,
) -> None:
    """Ensure that crop dimensions and focus offsets retain their positions."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
