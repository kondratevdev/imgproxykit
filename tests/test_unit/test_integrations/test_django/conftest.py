import pytest
from django.conf import LazySettings


@pytest.fixture(autouse=True)
def _configure_imgproxy(settings: LazySettings) -> None:
    """Provide the default Django adapter configuration."""
    settings.IMGPROXYKIT = {'client': {'base_url': 'https://example.com'}}
