# Optional integration tests require their framework.
# flake8: noqa: WPS412
import pytest

try:  # noqa: RUF067
    import django  # noqa: F401  # pyright: ignore[reportUnusedImport]
except ImportError:  # pragma: no cover
    pytest.skip(reason='django is not installed', allow_module_level=True)
