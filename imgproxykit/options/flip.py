from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, kw_only=True)
class Flip(Option):
    """
    Flip the image horizontally and/or vertically.

    Omitted axes remain ``None`` and use
    imgproxy defaults.

    Attributes:
        horizontal: Whether to mirror the image horizontally.
        vertical: Whether to mirror the image vertically.

    Usage:

    >>> option = Flip(horizontal=True)
    >>> option.arguments
    (True, None)
    >>> option = Flip(horizontal=True, vertical=True)
    >>> option.arguments
    (True, True)

    See `imgproxy flip
    <https://docs.imgproxy.net/usage/processing#flip>`_.
    """

    horizontal: bool | None = None
    vertical: bool | None = None

    name: ClassVar[str] = 'flip'
    short_name: ClassVar[str | None] = 'fl'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.horizontal, self.vertical)
