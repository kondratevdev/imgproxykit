from http import HTTPStatus

import pytest
import zapros
from inline_snapshot import snapshot


@pytest.mark.asyncio
async def test_image_url(fastapi_client: zapros.AsyncClient) -> None:
    """Return a signed image URL through the FastAPI integration."""
    response = await fastapi_client.get(
        '/images',
        params={'source': 's3://images/photo.jpg'},
    )

    assert response.status == HTTPStatus.OK
    assert response.json == snapshot({
        'url': 'http://localhost:10002/'
        'L0RDdxi3h1d9jV7NThc_36IC9chNMxBMoBRJIovd1gM/'
        'width:640/format:webp/'
        'czM6Ly9pbWFnZXMvcGhvdG8uanBn',
    })
