from collections.abc import Iterator
from pathlib import Path
from typing import Final

import pytest
import zapros
from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HttpWaitStrategy

from imgproxykit import Client

_PORT: Final = 8080
# Fixed test credentials; the client and server must use the same pair.
_KEY: Final = '736563726574'
_SALT: Final = '73616c74'


@pytest.fixture(scope='session')
def image_fixtures() -> Path:
    """Return the directory containing local image fixtures."""
    # source.png: solid red, 640x480, for resizing, formats, and headers.
    # pattern.png: 80x60, red/green above blue/yellow, for crop and flip checks.
    # transparent.png: 80x60, red center and clear edges, for background checks.
    return Path(__file__).parent.parent / 'fixtures'


@pytest.fixture(scope='session')
def imgproxy_image() -> str:
    """Return the pinned imgproxy image used by integration tests."""
    # PreserveHDR requires imgproxy 4; pin the version for repeatable tests.
    return 'ghcr.io/imgproxy/imgproxy:v4.0.0'


@pytest.fixture
def http_client() -> Iterator[zapros.Client]:
    """Provide an HTTP client with a timeout and automatic cleanup."""
    with zapros.Client(zapros.StdNetworkHandler(total_timeout=10)) as client:
        yield client


@pytest.fixture(scope='session')
def imgproxy_url(
    imgproxy_image: str,
    image_fixtures: Path,
) -> Iterator[str]:
    """Provide the base URL of a ready imgproxy container."""
    # Copying the directory preserves its name: /data/fixtures/*.png.
    # local:/// URLs read these files without an external image server.
    container = (
        DockerContainer(imgproxy_image)  # noqa: WPS221
        .with_exposed_ports(_PORT)
        .with_env('IMGPROXY_KEY', _KEY)
        .with_env('IMGPROXY_SALT', _SALT)
        .with_env('IMGPROXY_LOCAL_FILESYSTEM_ROOT', '/data/fixtures')
        .with_env('IMGPROXY_WATERMARK_PATH', '/data/fixtures/transparent.png')
        .with_env('IMGPROXY_ALLOW_SECURITY_OPTIONS', 'true')
        .with_copy_into_container(image_fixtures, '/data')
    )
    # Different sizes make preset ordering observable in the resulting image.
    container.with_env(
        'IMGPROXY_PRESETS',
        'thumbnail=resize:fill:160:120,small=resize:fill:80:60',
    )
    # Reuse the same image under a name that exercises UTF-8 and spaces.
    container.with_copy_into_container(
        image_fixtures / 'source.png',
        '/data/fixtures/café photo.png',
    )
    container.waiting_for(HttpWaitStrategy(_PORT, '/health'))
    with container:
        host = container.get_container_host_ip()
        port = container.get_exposed_port(_PORT)
        yield f'http://{host}:{port}'


@pytest.fixture
def imgproxy_client(imgproxy_url: str) -> Client:
    """Provide a signed client connected to imgproxy."""
    return Client(imgproxy_url, key=_KEY, salt=_SALT)
