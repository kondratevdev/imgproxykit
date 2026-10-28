from http import HTTPStatus

from django.test import Client
from inline_snapshot import snapshot


def test_image_urls(client: Client) -> None:
    """Return a signed image URL and named variants through DRF."""
    response = client.get(
        '/api/images/',
        {'source': 's3://images/photo.jpg'},
        HTTP_ACCEPT='application/json',
    )

    assert response.status_code == HTTPStatus.OK
    assert response['Content-Type'] == 'application/json'
    assert response.json() == snapshot({
        'url': 'http://localhost:10002/'
        'L0RDdxi3h1d9jV7NThc_36IC9chNMxBMoBRJIovd1gM/'
        'width:640/format:webp/czM6Ly9pbWFnZXMvcGhvdG8uanBn',
        'variants': {
            'small': 'http://localhost:10002/'
            'TTVXMU0mo9xIxb_wpkxJLOy-mnWf-INwt8GUmo9BydQ/'
            'width:320/format:webp/czM6Ly9pbWFnZXMvcGhvdG8uanBn',
            'medium': 'http://localhost:10002/'
            'L0RDdxi3h1d9jV7NThc_36IC9chNMxBMoBRJIovd1gM/'
            'width:640/format:webp/czM6Ly9pbWFnZXMvcGhvdG8uanBn',
            'large': 'http://localhost:10002/'
            'K8NJsvWAZYZFY205hJlWifYG6c_ToVZVNjfQW-xAu78/'
            'width:1280/format:webp/czM6Ly9pbWFnZXMvcGhvdG8uanBn',
        },
    })
