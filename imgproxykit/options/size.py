from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, kw_only=True)
class Size(Option):
    """
    Set target dimensions, upscaling, and canvas extension.

    Values left as ``None`` are not supplied
    explicitly; imgproxy resolves their defaults.

    Attributes:
        width: Target width in pixels.
        height: Target height in pixels.
        enlarge: Allow upscaling smaller source images.
        extend: Pad images smaller than the target dimensions.

    Usage:

    >>> option = Size(width=300, height=200, enlarge=True)
    >>> option.arguments
    (300, 200, True, None)

    See `imgproxy size
    <https://docs.imgproxy.net/usage/processing#size>`_.

    """

    width: int | None = None
    height: int | None = None
    enlarge: bool | None = None
    extend: bool | None = None

    name: ClassVar[str] = 'size'
    short_name: ClassVar[str | None] = 's'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.width, self.height, self.enlarge, self.extend)
