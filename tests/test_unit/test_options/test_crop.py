import pytest

from imgproxykit.options import Crop, Gravity
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Crop(), 'crop'),
        (Crop(gravity=Gravity.smart()), 'crop:::sm'),
        (Crop(gravity=Gravity.center(offset_y=0)), 'crop:::ce::0'),
        (
            Crop(
                width=0.5,
                height=0.75,
                gravity=Gravity.focus(x=0.25, y=0.125),
            ),
            'crop:0.5:0.75:fp:0.25:0.125',
        ),
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
