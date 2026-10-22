import pytest

from imgproxykit.options import Zoom
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Zoom(factor_x=1.5), 'zoom:1.5'),
        (Zoom(factor_x=1.5, factor_y=2.5), 'zoom:1.5:2.5'),
    ],
)
def test_zoom(
    path_serializer: PathSerializer,
    *,
    option: Zoom,
    expected: str,
) -> None:
    """Ensure that zoom supports uniform and independent axis factors."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
