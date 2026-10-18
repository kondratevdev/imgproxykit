from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class Height(Option):
    """
    Set the target height in pixels.

    Zero lets imgproxy calculate height from width and aspect ratio.
    With force resizing, zero preserves the source height.

    Attributes:
        value: Target height in pixels.

    Usage:

    >>> option = Height(200)
    >>> option.arguments
    (200,)

    See `imgproxy height
    <https://docs.imgproxy.net/usage/processing#height>`_.

    """

    value: int

    _name: ClassVar[OptionType] = 'h'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
