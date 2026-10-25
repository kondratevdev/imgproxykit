# Optional integrations check their dependencies before importing adapters.
# flake8: noqa: WPS412
try:  # noqa: RUF067
    import django  # noqa: F401  # pyright: ignore[reportUnusedImport]
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        'The Django integration requires Django. '
        "Install it with `pip install 'imgproxykit[django]'`.",
    ) from exc

from imgproxykit.integrations.django.client import get_client as get_client
from imgproxykit.integrations.django.settings import (
    ClientSettings as ClientSettings,
)
from imgproxykit.integrations.django.settings import (
    ClientSettingsDict as ClientSettingsDict,
)
from imgproxykit.integrations.django.settings import (
    Settings as Settings,
)
from imgproxykit.integrations.django.settings import (
    SettingsDict as SettingsDict,
)
from imgproxykit.integrations.django.shortcuts import (
    imgproxy_url as imgproxy_url,
)
from imgproxykit.integrations.django.shortcuts import (
    imgproxy_variants as imgproxy_variants,
)
