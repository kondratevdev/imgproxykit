import pytest

from imgproxykit.options import CacheBuster
from imgproxykit.serialization import PathSerializer


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (CacheBuster(value=''), 'cachebuster:'),
        (CacheBuster(value='v1'), 'cachebuster:v1'),
        (
            CacheBuster(value='café /:%?#'),
            'cachebuster:caf%C3%A9%20%2F%3A%25%3F%23',
        ),
    ],
)
def test_cache_buster(
    path_serializer: PathSerializer,
    *,
    option: CacheBuster,
    expected: str,
) -> None:
    """Ensure that cache busters escape reserved characters and Unicode."""
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == expected
    )
