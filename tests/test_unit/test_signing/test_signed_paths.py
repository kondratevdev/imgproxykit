from typing import Final

import pytest
from faker import Faker

from imgproxykit.signing import URLSigner

_KEY: Final = '736563726574'
_SALT: Final = '73616c74'


def test_unsigned_path(faker: Faker) -> None:
    """Ensure that omitted credentials select the unsafe marker."""
    assert URLSigner()(faker.file_path()) == 'unsafe'


@pytest.mark.parametrize(
    ('path', 'expected'),
    [
        (
            '/rs:fill:300:200/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc.webp',
            'IFOHEnjwIOnwbBU8WexRy_3nv99lVipxJG_F6tiWiKY',
        ),
        (
            '/café/naïve.jpg',
            'ZN61oYlsd53IQaf_0-oqrAi9eBYyCLJrkYNriTUOkGE',
        ),
        ('/a/../b', 'CSsxSKjH31lwRHIcZ_mhhYmN0Z-Wj8nbQP5x8qDc_F8'),
        ('/b', 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'),
    ],
)
def test_signed_path(*, path: str, expected: str) -> None:
    """Ensure that the exact UTF-8 path matches independent test vectors."""
    # Vectors use OpenSSL HMAC-SHA256 with key b'secret' and salt b'salt'.
    signer = URLSigner(key=_KEY, salt=_SALT)

    assert signer(path) == expected


def test_signer_reuse(faker: Faker) -> None:
    """Ensure that signing another path does not change previous signatures."""
    signer = URLSigner(key=_KEY, salt=_SALT)

    path = faker.file_path()
    signature = signer(path)
    signer(f'{path}/other')

    assert signer(path) == signature
