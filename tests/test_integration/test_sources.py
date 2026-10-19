import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Format
from tests.test_integration.assertions import assert_image


def test_unicode_source(
    imgproxy_client: Client,
    http_client: zapros.Client,
) -> None:
    """Ensure that source names retain Unicode and spaces through encoding."""
    url = imgproxy_client.url(
        'local:///café photo.png',
        transform=Transform(Format('png')),
    )

    response = http_client.get(url)

    assert_image(response, format='PNG', size=(640, 480))
