from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class Blur(Option):
    """
    Apply Gaussian blur with the given sigma.

    The sigma controls the size of the Gaussian blur mask.

    Attributes:
        value: Gaussian blur sigma.

    Usage:

    >>> option = Blur(2.0)
    >>> option.arguments
    (2.0,)

    See `imgproxy blur
    <https://docs.imgproxy.net/usage/processing#blur>`_.

    """

    value: float

    _name: ClassVar[OptionType] = 'bl'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
