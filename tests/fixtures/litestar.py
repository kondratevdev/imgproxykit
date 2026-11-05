from collections.abc import AsyncIterator

import pytest
import zapros


@pytest.fixture
async def litestar_client() -> AsyncIterator[zapros.AsyncClient]:
    """Provide an HTTP client for the runnable Litestar application."""
    from test_apps.litestar.app import app  # noqa: PLC0415

    async with zapros.AsyncClient(
        handler=zapros.AsgiHandler(app),
        base_url='http://testserver',
    ) as client:
        yield client
