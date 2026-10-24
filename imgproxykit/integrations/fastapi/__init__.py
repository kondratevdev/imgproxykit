# Optional integrations check their dependencies before importing adapters.
# flake8: noqa: WPS412
try:  # noqa: RUF067
    import fastapi  # noqa: F401  # pyright: ignore[reportUnusedImport]
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        'The FastAPI integration requires FastAPI. '
        "Install it with `pip install 'imgproxykit[fastapi]'`.",
    ) from exc

from imgproxykit.integrations.fastapi.dependencies import (
    add_imgproxy as add_imgproxy,
)
