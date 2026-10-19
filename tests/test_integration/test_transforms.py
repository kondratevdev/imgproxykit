from typing import Final

import pytest
import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Resize
from imgproxykit.types import FormatType
from tests.test_integration.assertions import assert_image

_WIDTH: Final = 160
_HEIGHT: Final = 120


@pytest.mark.parametrize(
    ('output_format', 'expected_format', 'content_type'),
    [
        ('webp', 'WEBP', 'image/webp'),
        ('png', 'PNG', 'image/png'),
        ('jpg', 'JPEG', 'image/jpeg'),
    ],
)
def test_signed_resize(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    output_format: FormatType,
    expected_format: str,
    content_type: str,
) -> None:
    """Ensure that signed transforms select the expected size and format."""
    transform = Transform(
        Resize(width=_WIDTH, height=_HEIGHT, mode='fill'),
        format=output_format,
    )
    url = imgproxy_client.url('local:///source.png', transform=transform)

    response = http_client.get(url)

    assert response.headers['Content-Type'] == content_type
    assert_image(
        response.read(),
        format=expected_format,
        size=(_WIDTH, _HEIGHT),
    )


def test_resize_height(
    imgproxy_client: Client,
    http_client: zapros.Client,
) -> None:
    """Ensure that omitted resize arguments preserve source proportions."""
    transform = Transform(Resize(height=_HEIGHT))
    url = imgproxy_client.url('local:///source.png', transform=transform)

    response = http_client.get(url)

    assert_image(response.read(), size=(_WIDTH, _HEIGHT))
