import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Resize


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Resize(), 'resize'),
        (
            Resize(
                width=300,
                height=200,
                mode='fill',
                enlarge=False,
                extend=True,
            ),
            'resize:fill:300:200:0:1',
        ),
        (Resize(height=200), 'resize:::200'),
        (Resize(extend=False), 'resize:::::0'),
    ],
)
def test_resize(*, option: Resize, expected: str) -> None:
    """Ensure that resize arguments follow protocol order and retain gaps."""
    assert serialize_option(option) == expected
