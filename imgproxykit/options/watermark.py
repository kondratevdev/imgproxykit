from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType, WatermarkPosition


@dataclass(frozen=True, slots=True, kw_only=True)
class Watermark(Option):
    """
    Apply the watermark image configured on the imgproxy server.

    Omitted settings remain :data:`~imgproxykit.types.EMPTY` and are
    resolved by the server.

    Attributes:
        opacity: Multiplier applied to the configured base opacity.
        position: Watermark anchor, or ``re`` to repeat it across the image.
        offset_x: Horizontal offset, or horizontal spacing when repeating.
        offset_y: Vertical offset, or vertical spacing when repeating.
        scale: Size relative to the resulting image. Zero or omission
            preserves the watermark size.

    Usage:

    >>> option = Watermark(
    ...     opacity=0.5, position='soea', offset_x=10, offset_y=10
    ... )
    >>> option.arguments
    (0.5, 'soea', 10, 10, EMPTY)

    See `imgproxy watermark
    <https://docs.imgproxy.net/usage/processing#watermark>`_
    and `watermark image configuration
    <https://docs.imgproxy.net/features/watermark#specifying-watermark-image>`_.

    """

    # Public API:
    opacity: float
    position: WatermarkPosition | EMPTY = EMPTY
    offset_x: float | EMPTY = EMPTY
    offset_y: float | EMPTY = EMPTY
    scale: float | EMPTY = EMPTY

    # Public API:
    name: ClassVar[OptionType] = 'watermark'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.opacity,
            self.position,
            self.offset_x,
            self.offset_y,
            self.scale,
        )
