import pytest
from fastapi import FastAPI, Request

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy
from tests.fixtures.credentials import Credentials


@pytest.mark.asyncio
async def test_registered_client(
    app: FastAPI,
    client: Client,
    asgi_request: Request,
) -> None:
    """Return the client registered under the default name."""
    dependency = add_imgproxy(app, client)

    assert app.state.imgproxykit_client is client
    assert await dependency(asgi_request) is client


@pytest.mark.asyncio
async def test_named_client(
    app: FastAPI,
    client: Client,
    asgi_request: Request,
) -> None:
    """Return the client registered under an explicit name."""
    dependency = add_imgproxy(app, client, name='custom_client')

    assert app.state.custom_client is client
    assert await dependency(asgi_request) is client


@pytest.mark.asyncio
async def test_multiple_clients(
    app: FastAPI,
    client: Client,
    asgi_request: Request,
    credentials: Credentials,
) -> None:
    """Resolve signed and unsigned clients independently on one application."""
    signed = Client('https://images.example.com', **credentials)

    get_unsigned = add_imgproxy(app, client)
    get_signed = add_imgproxy(app, signed, name='signed')

    assert await get_unsigned(asgi_request) is client
    assert await get_signed(asgi_request) is signed


@pytest.mark.parametrize('registered', [False, True])
def test_occupied_attribute(
    app: FastAPI,
    client: Client,
    *,
    registered: bool,
) -> None:
    """Preserve an occupied attribute, including an existing None value."""
    occupied = client if registered else None
    app.state.imgproxykit_client = occupied

    with pytest.raises(ValueError, match='already has an attribute'):
        add_imgproxy(app, client)

    assert app.state.imgproxykit_client is occupied


@pytest.mark.asyncio
async def test_missing_client(
    client: Client,
    asgi_request: Request,
) -> None:
    """Report a missing registration when resolving the dependency."""
    dependency = add_imgproxy(FastAPI(), client)

    with pytest.raises(TypeError, match='Call add_imgproxy'):
        await dependency(asgi_request)
