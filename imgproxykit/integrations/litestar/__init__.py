# Optional integrations check their dependencies before importing adapters.
# flake8: noqa: WPS412
try:  # noqa: RUF067
    import litestar  # noqa: F401  # pyright: ignore[reportUnusedImport]
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        'The Litestar integration requires Litestar. '
        "Install it with `pip install 'imgproxykit[litestar]'`.",
    ) from exc

from imgproxykit.integrations.litestar.plugin import (
    ImgproxyPlugin as ImgproxyPlugin,
)
