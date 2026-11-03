import pytest

from imgproxykit.options import ResizingAlgorithm
from imgproxykit.serialization import PathSerializer
from imgproxykit.types import ResizingAlgorithmType


@pytest.mark.parametrize(
    'algorithm',
    ['nearest', 'linear', 'cubic', 'lanczos2', 'lanczos3'],
)
def test_resizing_algorithm(
    path_serializer: PathSerializer,
    *,
    algorithm: ResizingAlgorithmType,
) -> None:
    """Ensure that resizing algorithms use the resizing algorithm segment."""
    option = ResizingAlgorithm(value=algorithm)

    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == f'resizing_algorithm:{algorithm}'
    )
