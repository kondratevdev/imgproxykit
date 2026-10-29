from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, ResizeType


@dataclass(frozen=True, slots=True, kw_only=True)
class Resize(Option):
    """
    Configure image dimensions and resizing behavior.

    Values left as ``None`` are not supplied
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
    ('fill', 96, 96, None, None)

    See `imgproxy resize
    <https://docs.imgproxy.net/usage/processing#resize>`_.

    """

    # Public API:
    width: int | None = None
    height: int | None = None
    mode: ResizeType | None = None
    enlarge: bool | None = None
    extend: bool | None = None

    # Public API:
    name: ClassVar[str] = 'resize'
    short_name: ClassVar[str | None] = 'rs'

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
