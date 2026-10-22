import pytest

from imgproxykit.signing import UrlSigner
from tests.fixtures.credentials import Credentials


@pytest.fixture
def url_signer(credentials: Credentials) -> UrlSigner:
    """Provide a signer with the shared credentials and full digest."""
    return UrlSigner(
        **credentials,
        signature_size=32,
        unsigned_signature='unsafe',
    )


@pytest.fixture
def unsigned_url_signer() -> UrlSigner:
    """Provide a signer configured for unsigned paths."""
    return UrlSigner(
        key=None,
        salt=None,
        signature_size=32,
        unsigned_signature='unsafe',
    )
