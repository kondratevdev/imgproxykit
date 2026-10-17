from typing import Final

import pytest

from imgproxykit.signing import URLSigner

_KEY: Final = '736563726574'
_SALT: Final = '73616c74'


@pytest.mark.parametrize(
    ('signature_size', 'expected'),
    [
        (1, 'pA'),
        (16, 'pEIkEjcNKr42hrTpB8MBuw'),
        (32, 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'),
        (33, 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'),
    ],
)
def test_signature_size(*, signature_size: int, expected: str) -> None:
    """Ensure that digest bytes are truncated before Base64 encoding."""
    signer = URLSigner(key=_KEY, salt=_SALT, signature_size=signature_size)

    assert signer('/b') == expected


@pytest.mark.parametrize('signature_size', [-1, 0])
def test_invalid_signature_size(*, signature_size: int) -> None:
    """Ensure that invalid sizes fail even in unsigned mode."""
    with pytest.raises(ValueError, match='signature_size must be positive'):
        URLSigner(signature_size=signature_size)
