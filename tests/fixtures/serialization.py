import pytest

from imgproxykit.serialization import PathSerializer


@pytest.fixture
def path_serializer() -> PathSerializer:
    """Provide a serializer with the standard argument separator."""
    return PathSerializer(arguments_separator=':')
