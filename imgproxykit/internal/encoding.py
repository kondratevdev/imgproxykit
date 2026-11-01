import base64
from urllib.parse import quote


def encode_plain(value: str) -> str:
    """
    Percent-encode a source URL for imgproxy's plain source URL mode.

    imgproxy permits full percent-encoding or escaping only ``%``, ``?``,
    and ``@``. Use full UTF-8 percent-encoding to keep source URL characters
    from affecting the outer URL. Existing escapes are encoded too:
    ``%20`` becomes ``%2520``, preserving it after outer URL decoding.

    See `imgproxy plain source URLs
    <https://docs.imgproxy.net/usage/processing#plain>`_.
    """
    return quote(value, safe='')


def encode_base64(value: str | bytes) -> str:
    """
    Encode text or bytes as URL-safe Base64 without padding.

    Text is first encoded as UTF-8. Byte values, such as signature digests,
    are encoded directly. Trailing ``=`` padding is removed for URL paths.

    See `imgproxy base64 source URLs
    <https://docs.imgproxy.net/usage/processing#base64-encoded>`_.
    """
    raw = value.encode() if isinstance(value, str) else value
    return base64.urlsafe_b64encode(raw).rstrip(b'=').decode()
