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
    ('output_format', 'expected_format'),
    [('webp', 'WEBP'), ('png', 'PNG'), ('jpg', 'JPEG')],
)
def test_signed_resize(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    output_format: FormatType,
    expected_format: str,
) -> None:
    """Ensure that signed transforms select the expected size and format."""
    transform = Transform(
        Resize(width=_WIDTH, height=_HEIGHT, mode='fill'),
        format=output_format,
    )
    url = imgproxy_client.url('local:///source.png', transform=transform)

    response = http_client.get(url)

    assert_image(response, format=expected_format, size=(_WIDTH, _HEIGHT))


def test_resize_height(
    imgproxy_client: Client,
    http_client: zapros.Client,
) -> None:
    """Ensure that omitted resize arguments preserve source proportions."""
    transform = Transform(Resize(height=_HEIGHT), format='png')
    url = imgproxy_client.url('local:///source.png', transform=transform)

    response = http_client.get(url)

    assert_image(response, format='PNG', size=(_WIDTH, _HEIGHT))
