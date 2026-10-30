import pytest

from imgproxykit.internal.encoding import encode_base64, encode_plain


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        # Empty input:
        ('', ''),
        (b'', ''),
        # Two, one, and no padding characters:
        ('f', 'Zg'),
        ('fo', 'Zm8'),
        ('foo', 'Zm9v'),
        # Text is encoded as UTF-8:
        ('café', 'Y2Fmw6k'),
        # Binary input uses the URL-safe alphabet:
        (b'\xfb\xef', '--8'),
        (b'\xff\xff', '__8'),
    ],
)
def test_encode_base64(*, value: str | bytes, expected: str) -> None:
    """Ensure that text and bytes use URL-safe Base64 without padding."""
    assert encode_base64(value) == expected


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        # Empty input:
        ('', ''),
        # Unreserved characters remain unchanged:
        ('thumbnail-640_480~2.jpg', 'thumbnail-640_480~2.jpg'),
        # Source from https://docs.imgproxy.net/usage/processing#plain,
        # using the documented full percent-encoding alternative:
        (
            'http://example.com/images/curiosity.jpg',
            'http%3A%2F%2Fexample.com%2Fimages%2Fcuriosity.jpg',
        ),
        # The docs require escaping %, ?, and @; newly generated escapes
        # must not be escaped again:
        ('%?@', '%25%3F%40'),
        # Query parameters belong to the source, not the imgproxy URL:
        (
            'https://example.com/photo.jpg?width=640&height=480',
            (
                'https%3A%2F%2Fexample.com%2Fphoto.jpg'
                '%3Fwidth%3D640%26height%3D480'
            ),
        ),
        # Fragments must not become fragments of the outer URL:
        ('sprite.svg#logo', 'sprite.svg%23logo'),
        # Existing percent escapes survive decoding of the outer URL:
        ('summer%20holiday.jpg', 'summer%2520holiday.jpg'),
        # Spaces use percent encoding, while literal plus signs stay distinct:
        ('cats + dogs.jpg', 'cats%20%2B%20dogs.jpg'),
        # Text is encoded as UTF-8:
        ('café.jpg', 'caf%C3%A9.jpg'),
    ],
)
def test_encode_plain(*, value: str, expected: str) -> None:
    """Escape sources fully, preserving existing escapes and UTF-8 text."""
    assert encode_plain(value) == expected
