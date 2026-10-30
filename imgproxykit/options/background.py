from dataclasses import dataclass
from typing import ClassVar, Self, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, kw_only=True)
class Background(Option):
    """
    Fill the background with a hex or RGB color, or explicitly disable filling.

    Useful when converting transparent images to JPEG. Use :meth:`hex` or
    :meth:`rgb` to select a color, and :meth:`disabled` to override background
    filling set earlier in the request, including by a preset.

    Attributes:
        color: Hex color without a leading hash, or an RGB tuple with
            channel values from 0 to 255. Omission disables filling.

    Usage:

    >>> option = Background.hex('ffffff')
    >>> option.arguments
    ('ffffff',)
    >>> option = Background.rgb(red=255, green=255, blue=255)
    >>> option.arguments
    (255, 255, 255)
    >>> option = Background.disabled()
    >>> option.arguments
    (None,)

    See `imgproxy background
    <https://docs.imgproxy.net/usage/processing#background>`_.

    """

    color: str | tuple[int, int, int] | None = None

    name: ClassVar[str] = 'background'
    short_name: ClassVar[str | None] = 'bg'

    @classmethod
    def rgb(cls, *, red: int, green: int, blue: int) -> Self:
        """Fill the background using three required RGB channels."""
        return cls(color=(red, green, blue))

    @classmethod
    def hex(cls, color: str) -> Self:
        """Fill the background using a hex color without a leading hash."""
        return cls(color=color)

    @classmethod
    def disabled(cls) -> Self:
        """
        Explicitly disable background filling, including a preset's color.

        Emits the background option without arguments. Unlike omitting the
        option, this overrides background filling configured earlier in the
        request. Equivalent to ``Background()``.
        """
        return cls()

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return self.color if isinstance(self.color, tuple) else (self.color,)
