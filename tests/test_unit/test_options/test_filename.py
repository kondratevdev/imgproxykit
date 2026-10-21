import pytest

from imgproxykit.options import Filename
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Filename(value=''), 'filename::1'),
        (
            Filename(value='product photo.jpg'),
            'filename:cHJvZHVjdCBwaG90by5qcGc:1',
        ),
        (Filename(value='café'), 'filename:Y2Fmw6k:1'),
    ],
)
def test_filename(*, option: Filename, expected: str) -> None:
    """Ensure that filenames use Base64 encoding with the encoding flag."""
    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == expected
    )
