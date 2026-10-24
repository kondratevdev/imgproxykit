from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from fastapi import FastAPI


@pytest.fixture
def fastapi_app() -> 'FastAPI':
    """Create an application with independent state."""
    from fastapi import FastAPI  # noqa: PLC0415

    return FastAPI()
