from collections.abc import AsyncIterator
from typing import TYPE_CHECKING

import pytest
import zapros

if TYPE_CHECKING:
    from fastapi import FastAPI


@pytest.fixture
def fastapi_app() -> 'FastAPI':
    """Create an application with independent state."""
    from fastapi import FastAPI  # noqa: PLC0415

    return FastAPI()


@pytest.fixture
async def fastapi_client() -> AsyncIterator[zapros.AsyncClient]:
    """Provide an HTTP client for the runnable FastAPI application."""
    from test_apps.fastapi.app import app  # noqa: PLC0415

    async with zapros.AsyncClient(
        handler=zapros.AsgiHandler(app),
        base_url='http://testserver',
    ) as client:
        yield client
