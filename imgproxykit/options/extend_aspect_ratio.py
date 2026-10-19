from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType, Position


@dataclass(frozen=True, slots=True, kw_only=True)
class ExtendAspectRatio(Option):
    """
    Extend the canvas to the requested aspect ratio.

    Omitted settings remain :data:`~imgproxykit.types.EMPTY`. The default
    anchor is center without offsets; smart gravity is unsupported.

    Attributes:
        value: Whether canvas extension is enabled.
        gravity: Canvas anchor, such as ``ce``, ``so``, or ``fp``.
        offset_x: Horizontal gravity offset or focus X coordinate.
        offset_y: Vertical gravity offset or focus Y coordinate.

    Usage:

    >>> option = ExtendAspectRatio(value=True, gravity='so')
    >>> option.arguments
    (True, 'so', EMPTY, EMPTY)

    See `imgproxy extend aspect ratio
    <https://docs.imgproxy.net/usage/processing#extend-aspect-ratio>`_.

    """

    value: bool
    gravity: Position | EMPTY = EMPTY
    offset_x: float | EMPTY = EMPTY
    offset_y: float | EMPTY = EMPTY

    name: ClassVar[OptionType] = 'extend_aspect_ratio'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.value,
            self.gravity,
            self.offset_x,
            self.offset_y,
        )
