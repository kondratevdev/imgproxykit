from django.conf import LazySettings
from django.test import override_settings

from imgproxykit.integrations.django import get_client


def test_shared_client(settings: LazySettings) -> None:
    """Reuse the client between calls."""
    settings.IMGPROXYKIT = {'client': {'base_url': 'https://images.com'}}

    assert get_client() is get_client()


def test_client_configuration(settings: LazySettings) -> None:
    """Use the nested client options without forwarding adapter defaults."""
    settings.IMGPROXYKIT = {
        'client': {
            'base_url': 'https://images.example.com',
            'unsigned_signature': 'trusted',
        },
    }

    assert (
        get_client()
        .url('source')
        .startswith('https://images.example.com/trusted/')
    )


def test_override_client(settings: LazySettings) -> None:
    """Refresh the client on entry and exit of a settings override."""
    settings.IMGPROXYKIT = {'client': {'base_url': 'https://original.com'}}
    original = get_client()

    with override_settings(
        IMGPROXYKIT={'client': {'base_url': 'https://other.com'}},
    ):
        overridden = get_client()
        assert overridden is not original
        assert overridden.url('source').startswith('https://other.com/')

    assert get_client() is not overridden
    assert get_client().url('source') == original.url('source')


def test_unrelated_setting(settings: LazySettings) -> None:
    """Keep the cached client when an unrelated Django setting changes."""
    settings.IMGPROXYKIT = {'client': {'base_url': 'https://images.com'}}
    client = get_client()
    settings.DEBUG = True

    assert get_client() is client
