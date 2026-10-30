from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, Position


@dataclass(frozen=True, slots=True, kw_only=True)
class Extend(Option):
    """
    Extend the canvas to the target dimensions.

    Omitted settings remain ``None``. The default
    anchor is center without offsets; smart gravity is unsupported.

    Attributes:
        value: Whether canvas extension is enabled.
        gravity: Canvas anchor, such as ``ce``, ``so``, or ``fp``.
        offset_x: Horizontal gravity offset or focus X coordinate.
        offset_y: Vertical gravity offset or focus Y coordinate.

    Usage:

    >>> option = Extend(value=True, gravity='so')
    >>> option.arguments
    (True, 'so', None, None)

    See `imgproxy extend
    <https://docs.imgproxy.net/usage/processing#extend>`_.
    """

    value: bool
    gravity: Position | None = None
    offset_x: float | None = None
    offset_y: float | None = None

    name: ClassVar[str] = 'extend'
    short_name: ClassVar[str | None] = 'ex'

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
