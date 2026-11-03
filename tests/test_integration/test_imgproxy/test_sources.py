import zapros

from imgproxykit import Client
from tests.test_integration.test_imgproxy.assertions import assert_image


def test_unicode_source(
    imgproxy_client: Client,
    http_client: zapros.Client,
) -> None:
    """Ensure that source names retain Unicode and spaces through encoding."""
    url = imgproxy_client.url('local:///utf8 café.png')

    response = http_client.get(url)

    assert_image(response, size=(640, 480))
