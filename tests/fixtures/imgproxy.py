from collections.abc import Iterator
from pathlib import Path
from typing import Final

import pytest
from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HttpWaitStrategy

from imgproxykit import Client
from tests.fixtures.credentials import Credentials

_PORT: Final = 8080
# PreserveHDR requires imgproxy 4; pin the version for repeatable tests.
_IMAGE: Final = 'ghcr.io/imgproxy/imgproxy:v4.0.0'

# source.png: solid red, 640x480, for resizing, formats, and headers.
# pattern.png: 80x60, red/green above blue/yellow, for crop and flip checks.
# transparent.png: 80x60, red center and clear edges, for background checks.
_IMAGES: Final = Path(__file__).parent / 'images'


@pytest.fixture(scope='session')
def imgproxy_url(
    credentials: Credentials,
) -> Iterator[str]:
    """Provide the base URL of a ready imgproxy container."""
    container = (
        DockerContainer(_IMAGE)  # noqa: WPS221
        .with_exposed_ports(_PORT)
        .with_env('IMGPROXY_KEY', credentials['key'])
        .with_env('IMGPROXY_SALT', credentials['salt'])
        .with_env('IMGPROXY_LOCAL_FILESYSTEM_ROOT', '/data/images')
        .with_env('IMGPROXY_WATERMARK_PATH', '/data/images/transparent.png')
        .with_env('IMGPROXY_ALLOW_SECURITY_OPTIONS', 'true')
        # Different preset sizes make their ordering observable.
        .with_env(
            'IMGPROXY_PRESETS',
            'thumbnail=resize:fill:160:120,small=resize:fill:80:60',
        )
        .with_copy_into_container(_IMAGES, '/data')
        # Reuse the image under a name that exercises UTF-8 and spaces.
        .with_copy_into_container(
            _IMAGES / 'source.png',
            '/data/images/café photo.png',
        )
        .waiting_for(HttpWaitStrategy(_PORT, '/health'))
    )
    with container:
        host = container.get_container_host_ip()
        port = container.get_exposed_port(_PORT)
        yield f'http://{host}:{port}'


@pytest.fixture
def unsigned_imgproxy_client() -> Client:
    """Provide an unsigned URL builder without starting an imgproxy server."""
    return Client('https://images.example.com')


@pytest.fixture(params=[False, True])
def imgproxy_client(
    imgproxy_url: str,
    credentials: Credentials,
    request: pytest.FixtureRequest,
) -> Client:
    """Exercise signed imgproxy requests with full names and short aliases."""
    return Client(
        imgproxy_url,
        **credentials,
        use_short_options=bool(request.param),
    )
