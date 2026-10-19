from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType, Position


@dataclass(frozen=True, slots=True, kw_only=True)
class Gravity(Option):
    """
    Choose the image area retained when cropping.

    Omitted offsets remain :data:`~imgproxykit.types.EMPTY`.

    Attributes:
        position: Anchor such as ``ce`` (center), ``sm`` (smart),
            or ``fp`` (focus point).
        offset_x: Horizontal offset; with ``fp``, the focus X coordinate.
        offset_y: Vertical offset; with ``fp``, the focus Y coordinate.

    Usage:

    >>> option = Gravity(position='ce')
    >>> option.arguments
    ('ce', EMPTY, EMPTY)
    >>> option = Gravity(position='fp', offset_x=0.25, offset_y=0.5)
    >>> option.arguments
    ('fp', 0.25, 0.5)

    See `imgproxy gravity
    <https://docs.imgproxy.net/usage/processing#gravity>`_.

    """

    # TODO: Add readable typed factories such as Gravity.smart(),
    # Gravity.center(), and Gravity.focus(x=..., y=...) so common usage
    # does not require protocol codes. Distinguish focus coordinates from
    # anchor offsets; consider readable anchors for Crop and Watermark too.

    # Public API:
    position: Position
    offset_x: float | EMPTY = EMPTY
    offset_y: float | EMPTY = EMPTY

    # Public API:
    name: ClassVar[OptionType] = 'gravity'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.position, self.offset_x, self.offset_y)
