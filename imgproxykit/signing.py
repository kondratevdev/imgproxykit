import contextlib
import hmac
from typing import Final

from imgproxykit.internal.encoding import encode_base64

# TODO: move to init?
# imgproxy verifies URL signatures using HMAC-SHA256.
_SIGNATURE_DIGEST: Final = 'sha256'


class UrlSigner:
    """
    Sign imgproxy paths using a reusable key and salt pair.

    Used by :class:`~imgproxykit.Client` after path construction.
    Credentials are decoded once during initialization and reused for
    subsequent signatures. Passing ``None`` for both credentials enables
    unsigned mode.

    Subclass this signer and override :meth:`__call__` to customize signing.
    Set the subclass on :attr:`imgproxykit.Client.url_signer_cls` to use it
    in a client.

    """

    __slots__ = (
        '_credentials',
        '_signature_size',
        '_unsigned_signature',
    )

    def __init__(
        self,
        *,
        key: str | None,
        salt: str | None,
        signature_size: int,
        unsigned_signature: str,
    ) -> None:
        """
        Configure signing credentials or enable unsigned mode.

        Supply both ``key`` and ``salt`` to generate signatures. Pass ``None``
        for both to return the configured unsigned marker.
        The server must accept unsigned requests or trust that marker.

        Args:
            key: Nonempty hex-encoded signing key matching the server.
                Supply together with ``salt``; ``None`` selects unsigned mode.
            salt: Nonempty hex-encoded signing salt matching the server.
                Supply together with ``key``; ``None`` selects unsigned mode.
            signature_size: Positive digest byte count to encode. Must match
                the server's `IMGPROXY_SIGNATURE_SIZE
                <https://docs.imgproxy.net/latest/configuration/options#url-signature>`__.
                Values of 32 or more use the full digest.
            unsigned_signature: URL marker used when key and salt are both
                ``None``.
                With server signing enabled, configure this marker
                in `IMGPROXY_TRUSTED_SIGNATURES
                <https://docs.imgproxy.net/latest/configuration/options#url-signature>`__.

        Raises:
            ValueError: If only one signing credential is supplied, either
                is empty or invalid hex, or ``signature_size`` is not
                positive, even in unsigned mode.
        """
        # Signing requires a positive digest byte count.
        if signature_size < 1:
            raise ValueError('signature_size must be positive.')

        # Signing requires a complete key and salt pair.
        if (key is None) != (salt is None):
            raise ValueError('key and salt must be supplied together.')

        self._unsigned_signature = unsigned_signature
        self._signature_size = signature_size

        # Passing None for both credentials selects unsigned mode.
        if key is None or salt is None:
            self._credentials = None
            return

        self._credentials = (
            self._decode_hex(key),
            self._decode_hex(salt),
        )

    def __call__(self, path: str) -> str:
        """
        Sign the exact supplied path or return the unsigned marker.

        The signature is an HMAC-SHA256 digest of the salt followed by
        the UTF-8 encoded path. The path is neither normalized nor modified.

        Args:
            path: Finalized path beginning with ``/``, including processing
                options, the encoded source, and any output extension.
                Excludes the server address and signature segment.

        Returns:
            URL-safe Base64 signature without padding, or the unsigned
            marker when both signing credentials are ``None``.

        """
        if self._credentials is None:
            return self._unsigned_signature

        key, salt = self._credentials
        signature = hmac.digest(
            key,
            salt + path.encode(),
            _SIGNATURE_DIGEST,
        )
        return encode_base64(signature[: self._signature_size])

    def _decode_hex(self, value: str) -> bytes:
        """
        Decode a nonempty hexadecimal credential.

        Invalid and empty values raise :class:`ValueError`.
        """
        with contextlib.suppress(ValueError):
            decoded = bytes.fromhex(value)
            if decoded:
                return decoded

        raise ValueError('Signing credentials must be nonempty hex strings.')
