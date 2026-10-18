from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class Rotate(Option):
    """
    Rotate clockwise by a multiple of 90 degrees.

    Rotation follows EXIF orientation unless automatic rotation is disabled.

    Attributes:
        value: Clockwise angle in degrees; must be a multiple of 90.

    Usage:

    >>> option = Rotate(90)
    >>> option.arguments
    (90,)

    See `imgproxy rotate
    <https://docs.imgproxy.net/usage/processing#rotate>`_.

    """

    value: int

    _name: ClassVar[OptionType] = 'rot'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
