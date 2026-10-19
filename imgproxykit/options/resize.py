from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType, ResizeType


@dataclass(frozen=True, slots=True, kw_only=True)
class Resize(Option):
    """
    Configure image dimensions and resizing behavior.

    Values left as :data:`~imgproxykit.types.EMPTY` are not supplied
    explicitly; imgproxy resolves their defaults.

    Attributes:
        width: Target width in pixels.
        height: Target height in pixels.
        mode: Resizing strategy, such as ``fit`` or ``fill``.
        enlarge: Allow upscaling smaller source images.
        extend: Pad images that are smaller than the target dimensions.

    Usage:

    >>> option = Resize(width=96, height=96, mode='fill')
    >>> option.arguments
    ('fill', 96, 96, EMPTY, EMPTY)

    See `imgproxy resize
    <https://docs.imgproxy.net/usage/processing#resize>`_.

    """

    # Public API:
    width: int | EMPTY = EMPTY
    height: int | EMPTY = EMPTY
    mode: ResizeType | EMPTY = EMPTY
    enlarge: bool | EMPTY = EMPTY
    extend: bool | EMPTY = EMPTY

    # Public API:
    name: ClassVar[OptionType] = 'resize'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.mode,
            self.width,
            self.height,
            self.enlarge,
            self.extend,
        )
