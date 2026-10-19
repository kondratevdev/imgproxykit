from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@dataclass(frozen=True, slots=True, kw_only=True)
class Flip(Option):
    """
    Flip the image horizontally and/or vertically.

    Omitted axes remain :data:`~imgproxykit.types.EMPTY` and use
    imgproxy defaults.

    Attributes:
        horizontal: Whether to mirror the image horizontally.
        vertical: Whether to mirror the image vertically.

    Usage:

    >>> option = Flip(horizontal=True)
    >>> option.arguments
    (True, EMPTY)
    >>> option = Flip(horizontal=True, vertical=True)
    >>> option.arguments
    (True, True)

    See `imgproxy flip
    <https://docs.imgproxy.net/usage/processing#flip>`_.

    """

    horizontal: bool | EMPTY = EMPTY
    vertical: bool | EMPTY = EMPTY

    name: ClassVar[OptionType] = 'flip'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.horizontal, self.vertical)
