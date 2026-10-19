import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Padding


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Padding(), 'padding'),
        (
            Padding(
                top=10,
                right=20,
                bottom=30,
                left=40,
            ),
            'padding:10:20:30:40',
        ),
        (Padding(left=0), 'padding::::0'),
    ],
)
def test_padding(*, option: Padding, expected: str) -> None:
    """Ensure that padding uses CSS side order and retains omitted sides."""
    assert serialize_option(option) == expected
