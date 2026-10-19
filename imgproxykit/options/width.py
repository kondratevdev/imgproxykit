from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class Width(Option):
    """
    Set the target width in pixels.

    Zero lets imgproxy calculate width from height and aspect ratio.
    With force resizing, zero preserves the source width.

    Attributes:
        value: Target width in pixels.

    Usage:

    >>> option = Width(300)
    >>> option.arguments
    (300,)

    See `imgproxy width
    <https://docs.imgproxy.net/usage/processing#width>`_.

    """

    value: int

    name: ClassVar[OptionType] = 'width'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
