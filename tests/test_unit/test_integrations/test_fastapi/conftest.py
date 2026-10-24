import pytest
from fastapi import FastAPI, Request

from imgproxykit import Client


@pytest.fixture
def app() -> FastAPI:
    """Create an application with independent state."""
    return FastAPI()


@pytest.fixture
def client() -> Client:
    """Provide a URL builder without starting an imgproxy server."""
    return Client('https://images.example.com')


@pytest.fixture
def asgi_request(app: FastAPI) -> Request:
    """Provide the application context used by the dependency."""
    return Request({'type': 'http', 'app': app})
