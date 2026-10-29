from dataclasses import dataclass
from typing import ClassVar, override
from urllib.parse import quote

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True)
class CacheBuster(ScalarOption[str]):
    """
    Add an escaped version string to the signed URL to bypass caches.

    Changing the value produces a new URL for browser and CDN caches
    without changing image processing. Special characters are escaped.

    Attributes:
        value: Cache version string included in the signed path.

    Usage:

    >>> option = CacheBuster('v2')
    >>> option.arguments
    ('v2',)

    See `imgproxy cache buster
    <https://docs.imgproxy.net/usage/processing#cache-buster>`_.

    """

    name: ClassVar[str] = 'cachebuster'
    short_name: ClassVar[str | None] = 'cb'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (quote(self.value, safe=''),)
