from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class EnforceThumbnail(Option):
    """
    Use an embedded HEIC or AVIF thumbnail when available.

    Uses the embedded thumbnail instead of the main source image
    when available. Supported for HEIC and AVIF sources.

    Attributes:
        value: Whether to prefer an embedded thumbnail.

    Usage:

    >>> option = EnforceThumbnail(True)
    >>> option.arguments
    (True,)

    See `imgproxy enforce thumbnail
    <https://docs.imgproxy.net/usage/processing#enforce-thumbnail>`_.

    """

    value: bool

    name: ClassVar[OptionType] = 'enforce_thumbnail'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
