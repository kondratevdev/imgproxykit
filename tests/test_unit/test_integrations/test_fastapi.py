# Optional integration tests require their framework.
import pytest

try:
    from fastapi import FastAPI, Request
except ImportError:  # pragma: no cover
    pytest.skip(reason='fastapi is not installed', allow_module_level=True)


from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy
from tests.fixtures.credentials import Credentials


@pytest.fixture
def asgi_request(fastapi_app: FastAPI) -> Request:
    """Provide the application context used by the dependency."""
    return Request({'type': 'http', 'app': fastapi_app})


@pytest.mark.asyncio
async def test_registered_client(
    fastapi_app: FastAPI,
    unsigned_imgproxy_client: Client,
    asgi_request: Request,
) -> None:
    """Return the client registered under the default name."""
    dependency = add_imgproxy(fastapi_app, unsigned_imgproxy_client)

    assert fastapi_app.state.imgproxykit_client is unsigned_imgproxy_client
    assert await dependency(asgi_request) is unsigned_imgproxy_client


@pytest.mark.asyncio
async def test_named_client(
    fastapi_app: FastAPI,
    unsigned_imgproxy_client: Client,
    asgi_request: Request,
) -> None:
    """Return the client registered under an explicit name."""
    dependency = add_imgproxy(
        fastapi_app, unsigned_imgproxy_client, name='custom_client'
    )

    assert fastapi_app.state.custom_client is unsigned_imgproxy_client
    assert await dependency(asgi_request) is unsigned_imgproxy_client


@pytest.mark.asyncio
async def test_multiple_clients(
    fastapi_app: FastAPI,
    unsigned_imgproxy_client: Client,
    asgi_request: Request,
    credentials: Credentials,
) -> None:
    """Resolve signed and unsigned clients independently on one application."""
    signed = Client('https://images.example.com', **credentials)

    get_unsigned = add_imgproxy(fastapi_app, unsigned_imgproxy_client)
    get_signed = add_imgproxy(fastapi_app, signed, name='signed')

    assert await get_unsigned(asgi_request) is unsigned_imgproxy_client
    assert await get_signed(asgi_request) is signed


@pytest.mark.parametrize('registered', [False, True])
def test_occupied_attribute(
    fastapi_app: FastAPI,
    unsigned_imgproxy_client: Client,
    *,
    registered: bool,
) -> None:
    """Preserve an occupied attribute, including an existing None value."""
    occupied = unsigned_imgproxy_client if registered else None
    fastapi_app.state.imgproxykit_client = occupied

    with pytest.raises(ValueError, match='already has an attribute'):
        add_imgproxy(fastapi_app, unsigned_imgproxy_client)

    assert fastapi_app.state.imgproxykit_client is occupied


@pytest.mark.asyncio
async def test_missing_client(
    unsigned_imgproxy_client: Client,
    asgi_request: Request,
) -> None:
    """Report a missing registration when resolving the dependency."""
    dependency = add_imgproxy(FastAPI(), unsigned_imgproxy_client)

    with pytest.raises(TypeError, match='Call add_imgproxy'):
        await dependency(asgi_request)
