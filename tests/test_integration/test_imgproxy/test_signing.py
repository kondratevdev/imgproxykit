from http import HTTPStatus
from typing import Final, Literal

import pytest
import zapros

from imgproxykit import Client, Transform
from imgproxykit.options import Resize
from tests.fixtures.credentials import Credentials
from tests.test_integration.test_imgproxy.assertions import assert_image

_WIDTH: Final = 160
_HEIGHT: Final = 120


@pytest.mark.parametrize('credential', ['key', 'salt'])
def test_invalid_credentials(
    credentials: Credentials,
    imgproxy_url: str,
    http_client: zapros.Client,
    *,
    credential: Literal['key', 'salt'],
) -> None:
    """Ensure that imgproxy rejects signatures with a wrong key or salt."""
    changed = credentials.copy()
    changed[credential] = '00'
    client = Client(imgproxy_url, **changed)

    response = http_client.get(client.url('local:///source.png'))

    assert response.status == HTTPStatus.FORBIDDEN, response.text


@pytest.mark.parametrize(
    ('original', 'replacement'),
    [
        (':fill:160:120', ':fill:80:60'),
        ('bG9jYWw6Ly8vc291cmNlLnBuZw', 'bG9jYWw6Ly8vcGF0dGVybi5wbmc'),
        (':png/', ':webp/'),
    ],
)
def test_modified_path(
    imgproxy_client: Client,
    http_client: zapros.Client,
    *,
    original: str,
    replacement: str,
) -> None:
    """Ensure that changing a signed path invalidates its signature."""
    transform = Transform(
        Resize(width=_WIDTH, height=_HEIGHT, mode='fill'),
        format='png',
    )
    url = imgproxy_client.url('local:///source.png', transform=transform)

    response = http_client.get(url)

    assert_image(response.read(), size=(_WIDTH, _HEIGHT))
    assert original in url

    response = http_client.get(url.replace(original, replacement))
    assert response.status == HTTPStatus.FORBIDDEN, response.text


def test_unsigned_url(imgproxy_url: str, http_client: zapros.Client) -> None:
    """Ensure that a server requiring signatures rejects unsigned URLs."""
    client = Client(imgproxy_url)

    response = http_client.get(client.url('local:///source.png'))

    assert response.status == HTTPStatus.FORBIDDEN, response.text
