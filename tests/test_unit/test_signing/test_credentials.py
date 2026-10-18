import pytest
from faker import Faker

from imgproxykit.signing import UrlSigner
from imgproxykit.types import EMPTY


@pytest.fixture
def credentials(faker: Faker) -> dict[str, str]:
    """Provide valid hexadecimal signing credentials."""
    return {
        'key': faker.binary(length=32).hex(),  # noqa: WPS432
        'salt': faker.binary(length=16).hex(),  # noqa: WPS432
    }


@pytest.mark.parametrize('credential', ['key', 'salt'])
def test_different_credentials(
    credentials: dict[str, str],
    *,
    credential: str,
) -> None:
    """Ensure that changing either credential changes the signature."""
    signer = UrlSigner(key=credentials['key'], salt=credentials['salt'])
    replacement = bytearray.fromhex(credentials[credential])
    replacement[0] ^= 1
    changed = {**credentials, credential: replacement.hex()}

    changed_signer = UrlSigner(key=changed['key'], salt=changed['salt'])

    assert changed_signer('/b') != signer('/b')


def test_uppercase_credentials() -> None:
    """Ensure that both hexadecimal credentials are case insensitive."""
    assert UrlSigner(key='ABCDEF', salt='FEDCBA')('/b') == UrlSigner(
        key='abcdef',
        salt='fedcba',
    )('/b')


@pytest.mark.parametrize('credential', ['key', 'salt'])
def test_incomplete_credentials(
    credentials: dict[str, str],
    *,
    credential: str,
) -> None:
    """Ensure that signing requires both credentials together."""
    with pytest.raises(
        ValueError, match='key and salt must be supplied together'
    ):
        UrlSigner(
            key=EMPTY if credential == 'key' else credentials['key'],
            salt=EMPTY if credential == 'salt' else credentials['salt'],
        )


@pytest.mark.parametrize('invalid', ['', '   ', 'invalid', '0'])
@pytest.mark.parametrize('credential', ['key', 'salt'])
def test_invalid_credentials(
    credentials: dict[str, str],
    *,
    invalid: str,
    credential: str,
) -> None:
    """Ensure that either credential rejects empty or invalid hex data."""
    credentials[credential] = invalid

    with pytest.raises(
        ValueError,
        match='Signing credentials must be nonempty hex strings',
    ):
        UrlSigner(key=credentials['key'], salt=credentials['salt'])
