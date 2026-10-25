from http import HTTPStatus

from django.test import Client
from pytest_django.asserts import assertContains


def test_image_page(client: Client) -> None:
    """Render image URLs using configured transforms and variants."""
    response = client.get('/', {'source': 'https://example.com/photo.jpg'})

    assert response.status_code == HTTPStatus.OK
    assertContains(response, '/width:640/format:webp/')
    assertContains(response, '/width:320/format:webp/')
    assertContains(response, '/width:1280/format:webp/')
