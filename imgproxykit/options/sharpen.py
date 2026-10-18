from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class Sharpen(Option):
    """
    Apply sharpening with the given sigma.

    The sigma controls the size of the sharpening mask.

    Attributes:
        value: Sharpening filter sigma.

    Usage:

    >>> option = Sharpen(1.0)
    >>> option.arguments
    (1.0,)

    See `imgproxy sharpen
    <https://docs.imgproxy.net/usage/processing#sharpen>`_.

    """

    value: float

    _name: ClassVar[OptionType] = 'sh'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
