import pytest

from imgproxykit.signing import UrlSigner
from tests.fixtures.credentials import Credentials


@pytest.mark.parametrize(
    ('signature_size', 'expected'),
    [
        (1, 'pA'),
        (16, 'pEIkEjcNKr42hrTpB8MBuw'),
        (32, 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'),
        (33, 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'),
    ],
)
def test_signature_size(
    credentials: Credentials,
    *,
    signature_size: int,
    expected: str,
) -> None:
    """Ensure that digest bytes are truncated before Base64 encoding."""
    signer = UrlSigner(
        **credentials,
        signature_size=signature_size,
        unsigned_marker='unsafe',
    )

    assert signer('/b') == expected


@pytest.mark.parametrize('signature_size', [-1, 0])
def test_invalid_signature_size(*, signature_size: int) -> None:
    """Ensure that invalid sizes fail even in unsigned mode."""
    with pytest.raises(ValueError, match='signature_size must be positive'):
        UrlSigner(
            key=None,
            salt=None,
            signature_size=signature_size,
            unsigned_marker='unsafe',
        )
