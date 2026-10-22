import pytest

from imgproxykit.signing import UrlSigner


def test_unsigned_path(unsigned_url_signer: UrlSigner) -> None:
    """Ensure that omitted credentials select the unsafe marker."""
    assert unsigned_url_signer('/first') == 'unsafe'


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
def test_signed_path(
    url_signer: UrlSigner,
    *,
    path: str,
    expected: str,
) -> None:
    """Ensure that the exact UTF-8 path matches independent test vectors."""
    # Vectors use OpenSSL HMAC-SHA256 with key b'secret' and salt b'salt'.

    assert url_signer(path) == expected


def test_signer_reuse(url_signer: UrlSigner) -> None:
    """Ensure that signing another path does not change previous signatures."""
    path = '/first'
    signature = url_signer(path)
    url_signer('/second')

    assert url_signer(path) == signature
