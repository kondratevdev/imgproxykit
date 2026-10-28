# Optional integrations check their dependencies before importing adapters.
# flake8: noqa: WPS412
try:  # noqa: RUF067
    import rest_framework  # noqa: F401  # pyright: ignore[reportUnusedImport]
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        'The DRF integration requires Django REST Framework. '
        "Install it with `pip install 'imgproxykit[drf]'`.",
    ) from exc

from imgproxykit.integrations.drf.serializers import (
    ImgproxyURLField as ImgproxyURLField,
)
from imgproxykit.integrations.drf.serializers import (
    ImgproxyVariantsField as ImgproxyVariantsField,
)
