import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import SkipProcessing


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (SkipProcessing(formats=()), 'skip_processing'),
        (SkipProcessing(formats=('svg',)), 'skip_processing:svg'),
        (SkipProcessing(formats=('svg', 'gif')), 'skip_processing:svg:gif'),
    ],
)
def test_skip_processing(*, option: SkipProcessing, expected: str) -> None:
    """Ensure that skipped formats retain their order and allow omission."""
    assert serialize_option(option) == expected
