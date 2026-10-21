import pytest

from imgproxykit.options import SkipProcessing
from imgproxykit.serialization import PathSerializer


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
    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == expected
    )
