from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class MinHeight(Option):
    """
    Set the minimum resulting height in pixels.

    Combining this option with a target height can crop the result.

    Attributes:
        value: Minimum resulting height in pixels.

    Usage:

    >>> option = MinHeight(200)
    >>> option.arguments
    (200,)

    See `imgproxy min height
    <https://docs.imgproxy.net/usage/processing#min-height>`_.

    """

    value: int

    name: ClassVar[OptionType] = 'min-height'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
