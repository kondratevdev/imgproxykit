from collections.abc import Callable, Iterator, Mapping
from contextlib import ExitStack
from functools import cache
from pathlib import Path
from typing import Final, cast

import pytest
import yaml
from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HttpWaitStrategy

from imgproxykit import Client
from tests.fixtures.credentials import Credentials

_PORT: Final = 8080
# solid-red-640x480.png: resizing, formats, and response headers.
# color-quadrants-80x60.png: red/green above blue/yellow, for crop and flip.
# red-center-transparent-80x60.png: transparent edges, for background checks.
# utf8 café.png: solid red copy, for Unicode and spaces in source URLs.
_IMAGES: Final = Path(__file__).parent / 'images'

type _Environment = frozenset[tuple[str, str]]
type _ServerFactory = Callable[[_Environment], str]


def _get_imgproxy_image() -> str:
    """Read the pinned image shared with the manual Compose playground."""
    compose_path = Path(__file__).resolve().parents[2] / 'docker-compose.yaml'
    compose = yaml.safe_load(compose_path.read_text(encoding='utf-8'))
    return cast(str, compose['services']['imgproxy']['image'])


def _create_container(env: Mapping[str, str]) -> DockerContainer:
    """Build an imgproxy container with test images and explicit environment."""
    return (
        DockerContainer(_get_imgproxy_image())
        .with_envs(**env)
        .with_exposed_ports(_PORT)
        .with_copy_into_container(_IMAGES, '/data')
        .waiting_for(HttpWaitStrategy(_PORT, '/health'))
    )


@pytest.fixture(scope='session')
def imgproxy_env(credentials: Credentials) -> dict[str, str]:
    """Provide the default server environment shared by integration tests."""
    return {
        'IMGPROXY_KEY': credentials['key'],
        'IMGPROXY_SALT': credentials['salt'],
        'IMGPROXY_LOCAL_FILESYSTEM_ROOT': '/data/images',
    }


@pytest.fixture(scope='session')
def imgproxy_server() -> Iterator[_ServerFactory]:
    """
    Reuse ready servers with identical env throughout the test session.

    Start each configuration lazily and close all containers at session end.
    """
    with ExitStack() as stack:

        @cache
        def server(env: _Environment) -> str:  # noqa: WPS430
            container = stack.enter_context(_create_container(dict(env)))
            host = container.get_container_host_ip()
            port = container.get_exposed_port(_PORT)
            return f'http://{host}:{port}'

        yield server


def override_imgproxy_env(**env: str | None) -> pytest.MarkDecorator:
    """
    Override server env on a test, class, or parametrized case.

    Local settings override inherited ones. Use None to remove a default
    variable. Client signing settings must be configured separately.
    """
    return pytest.mark.imgproxy_env(**env)


@pytest.fixture
def imgproxy_url(
    imgproxy_server: _ServerFactory,
    imgproxy_env: dict[str, str],
    request: pytest.FixtureRequest,
) -> str:
    """Provide a shared server URL using defaults and local env overrides."""
    env = dict(imgproxy_env)

    for marker in reversed(list(request.node.iter_markers('imgproxy_env'))):
        for name, value in marker.kwargs.items():
            if value is None:
                env.pop(name, None)  # pragma: no cover
            else:
                env[name] = value

    return imgproxy_server(frozenset(env.items()))


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
