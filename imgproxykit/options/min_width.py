from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class MinWidth(Option):
    """
    Set the minimum resulting width in pixels.

    Combining this option with a target width can crop the result.

    Attributes:
        value: Minimum resulting width in pixels.

    Usage:

    >>> option = MinWidth(300)
    >>> option.arguments
    (300,)

    See `imgproxy min width
    <https://docs.imgproxy.net/usage/processing#min-width>`_.

    """

    value: int

    name: ClassVar[OptionType] = 'min-width'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
