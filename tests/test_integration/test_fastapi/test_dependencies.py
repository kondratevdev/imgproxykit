from http import HTTPStatus
from typing import Annotated

import pytest
import zapros
from fastapi import APIRouter, Depends, FastAPI

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy


@pytest.mark.asyncio
async def test_dependency_injection(
    fastapi_app: FastAPI,
    unsigned_imgproxy_client: Client,
) -> None:
    """FastAPI injects the registered client into a real route handler."""
    get_imgproxy = add_imgproxy(fastapi_app, unsigned_imgproxy_client)

    @fastapi_app.get('/check')
    async def check(  # noqa: WPS430
        injected: Annotated[Client, Depends(get_imgproxy)],
    ) -> bool:
        return injected is unsigned_imgproxy_client

    async with zapros.AsyncClient(
        handler=zapros.AsgiHandler(fastapi_app)
    ) as http:
        response = await http.get('http://testserver/check')

    assert response.status == HTTPStatus.OK
    assert response.json is True


@pytest.mark.asyncio
async def test_shared_router(
    fastapi_app: FastAPI,
    unsigned_imgproxy_client: Client,
) -> None:
    """A shared router resolves the client on the application serving it."""
    other = FastAPI()
    get_imgproxy = add_imgproxy(fastapi_app, unsigned_imgproxy_client)
    add_imgproxy(other, Client('https://second.example.com'))
    router = APIRouter()

    @router.get('/image')
    async def image(  # noqa: WPS430
        imgproxy: Annotated[Client, Depends(get_imgproxy)],
    ) -> str:
        return imgproxy.url('s3://images/photo.jpg')

    fastapi_app.include_router(router)
    other.include_router(router)

    async with zapros.AsyncClient(
        handler=zapros.AsgiHandler(fastapi_app)
    ) as http:
        assert (await http.get('http://testserver/image')).json == (
            'https://images.example.com/unsafe/czM6Ly9pbWFnZXMvcGhvdG8uanBn'
        )

    async with zapros.AsyncClient(handler=zapros.AsgiHandler(other)) as http:
        assert (await http.get('http://testserver/image')).json == (
            'https://second.example.com/unsafe/czM6Ly9pbWFnZXMvcGhvdG8uanBn'
        )
