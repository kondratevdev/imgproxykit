from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class Quality(Option):
    """
    Set output image quality.

    Attributes:
        value: Quality percentage. Zero delegates to server quality settings.

    Usage:

    >>> option = Quality(85)
    >>> option.arguments
    (85,)

    See `imgproxy quality
    <https://docs.imgproxy.net/usage/processing#quality>`_.

    """

    # Public API:
    value: int

    # Public API:
    name: ClassVar[OptionType] = 'quality'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
