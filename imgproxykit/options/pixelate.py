from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class Pixelate(Option):
    """
    Set the pixelation block size.

    Larger blocks produce a coarser pixelation effect.

    Attributes:
        value: Individual pixel block size in pixels.

    Usage:

    >>> option = Pixelate(10)
    >>> option.arguments
    (10,)

    See `imgproxy pixelate
    <https://docs.imgproxy.net/usage/processing#pixelate>`_.

    """

    value: int

    name: ClassVar[OptionType] = 'pixelate'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
