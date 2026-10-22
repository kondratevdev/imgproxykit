from typing import Literal

import pytest

from imgproxykit.signing import UrlSigner
from tests.fixtures.credentials import Credentials


@pytest.mark.parametrize('credential', ['key', 'salt'])
def test_incomplete_credentials(
    credentials: Credentials,
    *,
    credential: Literal['key', 'salt'],
) -> None:
    """Ensure that signing requires both credentials together."""
    with pytest.raises(
        ValueError,
        match='key and salt must be supplied together',
    ):
        UrlSigner(
            key=None if credential == 'key' else credentials['key'],
            salt=None if credential == 'salt' else credentials['salt'],
            signature_size=32,
            unsigned_signature='unsafe',
        )


@pytest.mark.parametrize('invalid', ['', '   ', 'invalid', '0'])
@pytest.mark.parametrize('credential', ['key', 'salt'])
def test_invalid_credentials(
    credentials: Credentials,
    *,
    invalid: str,
    credential: Literal['key', 'salt'],
) -> None:
    """Ensure that either credential rejects empty or invalid hex data."""
    changed = credentials.copy()
    changed[credential] = invalid

    with pytest.raises(
        ValueError,
        match='Signing credentials must be nonempty hex strings',
    ):
        UrlSigner(
            **changed,
            signature_size=32,
            unsigned_signature='unsafe',
        )
