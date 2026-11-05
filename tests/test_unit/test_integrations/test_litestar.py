# Optional integration tests require their framework.
import pytest

try:
    from litestar import Litestar
except ImportError:  # pragma: no cover
    pytest.skip(reason='litestar is not installed', allow_module_level=True)

from litestar.config.app import AppConfig
from litestar.di import Provide

from imgproxykit import Client
from imgproxykit.integrations.litestar import ImgproxyPlugin


@pytest.mark.asyncio
async def test_default_client(unsigned_imgproxy_client: Client) -> None:
    """Ensure that the default dependency returns the registered client."""
    app = Litestar(plugins=[ImgproxyPlugin(unsigned_imgproxy_client)])

    assert await app.dependencies['imgproxy']() is unsigned_imgproxy_client


@pytest.mark.asyncio
async def test_multiple_clients(
    unsigned_imgproxy_client: Client,
) -> None:
    """Ensure that named dependencies return their respective clients."""
    other_client = Client('https://other.example.com')
    app = Litestar(
        plugins=[
            ImgproxyPlugin(
                clients={
                    'default': unsigned_imgproxy_client,
                    'other': other_client,
                }
            ),
        ]
    )

    assert await app.dependencies['default']() is unsigned_imgproxy_client
    assert await app.dependencies['other']() is other_client


def test_dependency_conflict(unsigned_imgproxy_client: Client) -> None:
    """Ensure that a name conflict leaves all dependencies unchanged."""
    plugin = ImgproxyPlugin(
        clients={
            'available': unsigned_imgproxy_client,
            'occupied': unsigned_imgproxy_client,
        }
    )
    occupied = Provide(lambda: None, sync_to_thread=False)
    config = AppConfig(route_handlers=[], dependencies={'occupied': occupied})

    with pytest.raises(ValueError, match='already contain'):
        plugin.on_app_init(config)

    assert config.dependencies == {'occupied': occupied}


def test_missing_client_arguments() -> None:
    """Ensure that construction requires a client or a client mapping."""
    with pytest.raises(TypeError, match='Pass client or clients'):
        ImgproxyPlugin()  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]  # ty: ignore[no-matching-overload]


def test_conflicting_client_arguments(unsigned_imgproxy_client: Client) -> None:
    """Ensure that a client and a client mapping cannot be supplied together."""
    with pytest.raises(TypeError, match='not both'):
        ImgproxyPlugin(  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]  # ty: ignore[no-matching-overload]
            unsigned_imgproxy_client,
            clients={'custom': unsigned_imgproxy_client},
        )
