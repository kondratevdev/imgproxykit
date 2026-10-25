from functools import lru_cache
from typing import Any

from django.core.signals import setting_changed
from django.dispatch import receiver

from imgproxykit.client import Client
from imgproxykit.integrations.django.settings import (
    IMGPROXYKIT_SETTINGS,
    ClientSettings,
    Settings,
    get_config,
)


@lru_cache(maxsize=1)
def get_client() -> Client:
    """
    Return the cached client configured by IMGPROXYKIT['client'].

    Create the client on first use. Django's ``override_settings`` clears
    the cache when entering and leaving an override of ``IMGPROXYKIT``.
    """
    config = get_config()[Settings.client.value]
    # Client takes `base_url` positionally;
    # forward the remaining client options.
    options = {
        name: value
        for name, value in config.items()
        if name != ClientSettings.base_url
    }
    return Client(config[ClientSettings.base_url.value], **options)  # type: ignore[call-overload, no-any-return]  # pyright: ignore[reportCallIssue, reportArgumentType]  # ty: ignore[no-matching-overload]


@receiver(setting_changed)
def _reset_client(*, setting: str, **kwargs: Any) -> None:
    """Discard the cached client when Django overrides IMGPROXYKIT."""
    if setting == IMGPROXYKIT_SETTINGS:
        get_client.cache_clear()
