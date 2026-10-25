import pytest
from django.conf import LazySettings
from django.core.exceptions import ImproperlyConfigured

from imgproxykit import Transform
from imgproxykit.integrations.django.settings import get_config


def test_adapter_defaults(settings: LazySettings) -> None:
    """Add adapter defaults without changing the user's configuration."""
    settings.IMGPROXYKIT = {'client': {'base_url': 'https://images.com'}}

    assert get_config() == {
        'client': settings.IMGPROXYKIT['client'],
        'transforms': {},
        'variants': {},
        'source_resolver': (
            'imgproxykit.integrations.django.sources.default_source_resolver'
        ),
    }
    assert set(settings.IMGPROXYKIT) == {'client'}


def test_override_adapter_defaults(settings: LazySettings) -> None:
    """Keep explicitly configured adapter options."""
    thumbnail = Transform(width=160)
    settings.IMGPROXYKIT = {
        'client': {'base_url': 'https://images.example.com'},
        'transforms': {'thumbnail': thumbnail},
        'variants': {'responsive': {'small': thumbnail}},
        'source_resolver': 'custom.images.resolve_source',
    }

    assert get_config() == settings.IMGPROXYKIT


def test_none_configuration(settings: LazySettings) -> None:
    """Report an explicitly disabled configuration."""
    settings.IMGPROXYKIT = None

    with pytest.raises(ImproperlyConfigured, match='Define IMGPROXYKIT'):
        get_config()


def test_missing_configuration(settings: LazySettings) -> None:
    """Report an absent configuration."""
    settings.IMGPROXYKIT = None
    del settings.IMGPROXYKIT  # noqa: WPS420

    with pytest.raises(ImproperlyConfigured, match='Define IMGPROXYKIT'):
        get_config()
