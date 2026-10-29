from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, Position


@dataclass(frozen=True, slots=True, kw_only=True)
class Crop(Option):
    """
    Crop before resizing; dimensions below one are relative.

    Defines the source area to process before resizing. Omitted gravity
    uses the request gravity; omitted arguments remain
    ``None``.

    Attributes:
        width: Crop width: pixels at or above one, relative below one.
            Zero uses the full source width.
        height: Crop height: pixels at or above one, relative below one.
            Zero uses the full source height.
        gravity: Crop anchor, such as ``ce`` or ``fp``.
        offset_x: Horizontal gravity offset or focus X coordinate.
        offset_y: Vertical gravity offset or focus Y coordinate.

    Usage:

    >>> option = Crop(width=300, height=200, gravity='ce')
    >>> option.arguments
    (300, 200, 'ce', None, None)
    >>> option = Crop(
    ...     width=0.5, height=0.5, gravity='fp', offset_x=0.5, offset_y=0.5
    ... )
    >>> option.arguments
    (0.5, 0.5, 'fp', 0.5, 0.5)

    See `imgproxy crop
    <https://docs.imgproxy.net/usage/processing#crop>`_.

    """

    width: float | None = None
    height: float | None = None
    gravity: Position | None = None
    offset_x: float | None = None
    offset_y: float | None = None

    name: ClassVar[str] = 'crop'
    short_name: ClassVar[str | None] = 'c'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.width,
            self.height,
            self.gravity,
            self.offset_x,
            self.offset_y,
        )
