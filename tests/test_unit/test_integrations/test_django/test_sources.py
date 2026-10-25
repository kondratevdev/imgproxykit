from django.conf import LazySettings
from django.db.models.fields.files import FieldFile

from imgproxykit.integrations.django.sources import resolve_source


def _resolver(source: str | FieldFile) -> str:
    """Resolve a relative source to a storage URI."""
    return f's3://images/{source}'


def test_callable_resolver(settings: LazySettings) -> None:
    """Pass the original source to a callable resolver and return its URI."""
    settings.IMGPROXYKIT = {
        'client': {'base_url': 'https://example.com'},
        'source_resolver': _resolver,
    }

    assert resolve_source('photo.jpg') == 's3://images/photo.jpg'
