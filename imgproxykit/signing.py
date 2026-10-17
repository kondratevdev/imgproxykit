import contextlib
import hmac

from imgproxykit.internal.constants import SIGNATURE_DIGEST
from imgproxykit.internal.encoding import encode_base64
from imgproxykit.types import EMPTY


class URLSigner:
    """
    Sign imgproxy paths using a reusable key and salt pair.

    Used by :class:`~imgproxykit.Client` after path construction.
    Credentials are decoded once during initialization and reused for
    subsequent signatures. Omitting both credentials enables unsigned mode.

    Subclass this signer and override :meth:`__call__` to customize signing.
    Set the subclass on :attr:`imgproxykit.Client.signer_cls` to use it
    in a client.

    """

    __slots__ = (
        '_credentials',
        '_signature_size',
        '_unsigned_signature',
    )

    # Private API:
    _credentials: tuple[bytes, bytes] | None
    _signature_size: int

    def __init__(
        self,
        *,
        key: str | EMPTY = EMPTY,
        salt: str | EMPTY = EMPTY,
        signature_size: int = 32,
        unsigned_signature: str = 'unsafe',
    ) -> None:
        """
        Configure signing credentials or enable unsigned mode.

        Supply both credentials to generate signatures. Omit both to return
        the configured unsigned marker (``unsafe`` by default).

        Args:
            unsigned_signature: Marker returned without signing credentials.
                Defaults to 'unsafe'; custom values must be trusted by server.
            key: Nonempty hex-encoded signing key matching the server.
            salt: Nonempty hex-encoded signing salt matching the server.
            signature_size: Positive digest byte count to encode. Must match
                the server's IMGPROXY_SIGNATURE_SIZE. Defaults to 32.
                Values of 32 or more use the full digest.

        Raises:
            ValueError: If only one credential is supplied, or either
                credential is empty or contains invalid hexadecimal data,
                or signature_size is not positive.

        Usage:

        >>> from imgproxykit.signing import URLSigner
        >>> unsigned = URLSigner()
        >>> signed = URLSigner(
        ...     key='736563726574',
        ...     salt='73616c74',
        ... )

        These credentials are examples for local development.

        """
        # Signing requires a positive digest byte count.
        if signature_size < 1:
            raise ValueError('signature_size must be positive.')

        # Signing requires a complete key and salt pair.
        if (key is EMPTY) != (salt is EMPTY):
            raise ValueError('key and salt must be supplied together.')

        self._unsigned_signature = unsigned_signature
        self._signature_size = signature_size

        # Omitting both credentials selects unsigned mode.
        if key is EMPTY or salt is EMPTY:
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
            marker when signing credentials were omitted.

        """
        if self._credentials is None:
            return self._unsigned_signature

        key, salt = self._credentials
        signature = hmac.digest(
            key,
            salt + path.encode(),
            SIGNATURE_DIGEST,
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
