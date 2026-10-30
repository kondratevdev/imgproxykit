# Optional integration tests require their framework.
import pytest

try:
    import fastapi  # noqa: F401  # pyright: ignore[reportUnusedImport]
except ImportError:  # pragma: no cover
    pytest.skip(reason='fastapi is not installed', allow_module_level=True)

from http import HTTPStatus

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
        'url': (
            'http://localhost:10002/'
            'wWaQL2fIdx4tC8NALpxilcq2Kfv24AxRiRQB60l_bHE/'
            'format:webp/width:640/czM6Ly9pbWFnZXMvcGhvdG8uanBn'
        ),
    })


@pytest.mark.asyncio
async def test_image_variants(fastapi_client: zapros.AsyncClient) -> None:
    """Serialize dataclass variants through a Pydantic response DTO."""
    response = await fastapi_client.get(
        '/images/variants',
        params={'source': 's3://images/photo.jpg'},
    )

    assert response.status == HTTPStatus.OK
    assert response.json == snapshot({
        'images': {
            'thumbnail': (
                'http://localhost:10002/'
                'eMwawA59uE4G9Po9oBnS-6Dxr6U95oz7oEUp5YAnFBY/'
                'format:webp/width:320/czM6Ly9pbWFnZXMvcGhvdG8uanBn'
            ),
            'preview': (
                'http://localhost:10002/'
                'wWaQL2fIdx4tC8NALpxilcq2Kfv24AxRiRQB60l_bHE/'
                'format:webp/width:640/czM6Ly9pbWFnZXMvcGhvdG8uanBn'
            ),
        },
    })
