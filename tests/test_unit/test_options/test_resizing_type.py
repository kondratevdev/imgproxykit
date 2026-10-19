import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import ResizingType


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (ResizingType(value='fit'), 'resizing_type:fit'),
        (ResizingType(value='fill'), 'resizing_type:fill'),
        (ResizingType(value='auto'), 'resizing_type:auto'),
    ],
)
def test_resizing_type(*, option: ResizingType, expected: str) -> None:
    """Ensure that resizing strategies use the resizing type segment."""
    assert serialize_option(option) == expected
