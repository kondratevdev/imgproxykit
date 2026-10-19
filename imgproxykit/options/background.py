from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@dataclass(frozen=True, slots=True, kw_only=True)
class Background(Option):
    """
    Fill the background with a hex color or RGB tuple; omit to disable.

    Useful when converting transparent images to JPEG. Omit the color
    to disable background manipulation.

    Attributes:
        color: Hex color without a leading hash, or an RGB tuple with
            channel values from 0 to 255. Omission disables filling.

    Usage:

    >>> option = Background(color='ffffff')
    >>> option.arguments
    ('ffffff',)
    >>> option = Background(color=(255, 255, 255))
    >>> option.arguments
    (255, 255, 255)
    >>> option = Background()
    >>> option.arguments
    (EMPTY,)

    See `imgproxy background
    <https://docs.imgproxy.net/usage/processing#background>`_.

    """

    color: str | tuple[int, int, int] | EMPTY = EMPTY

    name: ClassVar[OptionType] = 'background'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return self.color if isinstance(self.color, tuple) else (self.color,)
