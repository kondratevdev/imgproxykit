from imgproxykit.options import ResizingType
from imgproxykit.serialization import PathSerializer


def test_resizing_type() -> None:
    """Ensure that resizing strategies use the resizing type segment."""
    option = ResizingType(value='fit')

    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == 'resizing_type:fit'
    )
