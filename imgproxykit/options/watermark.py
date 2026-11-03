from dataclasses import dataclass
from typing import ClassVar, Self, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, WatermarkPosition


@dataclass(frozen=True, slots=True, kw_only=True)
class Watermark(Option):  # noqa: WPS214
    """
    Apply the watermark image configured on the imgproxy server.

    Omitted settings remain ``None`` and are resolved by the server.
    Use the anchor factories to select a position or :meth:`repeat`
    to tile the watermark with optional spacing.

    Attributes:
        opacity: Multiplier applied to the configured base opacity.
        position: Watermark anchor, or ``re`` to repeat it across the image.
        offset_x: Horizontal offset, or horizontal spacing when repeating.
        offset_y: Vertical offset, or vertical spacing when repeating.
        scale: Size relative to the resulting image. Zero or omission
            preserves the watermark size.

    Usage:

    >>> option = Watermark.bottom_right(opacity=0.5, offset_x=10, offset_y=10)
    >>> option.arguments
    (0.5, 'soea', 10, 10, None)

    See `imgproxy watermark
    <https://docs.imgproxy.net/usage/processing#watermark>`_
    and `watermark image configuration
    <https://docs.imgproxy.net/features/watermark#specifying-watermark-image>`_.
    """

    opacity: float
    position: WatermarkPosition | None = None
    offset_x: float | None = None
    offset_y: float | None = None
    scale: float | None = None

    name: ClassVar[str] = 'watermark'
    short_name: ClassVar[str | None] = 'wm'

    @classmethod
    def center(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the center with optional offsets."""
        return cls(
            opacity=opacity,
            position='ce',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def top(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the top edge with optional offsets."""
        return cls(
            opacity=opacity,
            position='no',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def bottom(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the bottom edge with optional offsets."""
        return cls(
            opacity=opacity,
            position='so',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def left(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the left edge with optional offsets."""
        return cls(
            opacity=opacity,
            position='we',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def right(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the right edge with optional offsets."""
        return cls(
            opacity=opacity,
            position='ea',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def top_left(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the top-left corner with optional offsets."""
        return cls(
            opacity=opacity,
            position='nowe',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def top_right(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the top-right corner with optional offsets."""
        return cls(
            opacity=opacity,
            position='noea',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def bottom_left(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the bottom-left corner."""
        return cls(
            opacity=opacity,
            position='sowe',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def bottom_right(
        cls,
        *,
        opacity: float,
        offset_x: float | None = None,
        offset_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Place the watermark at the bottom-right corner."""
        return cls(
            opacity=opacity,
            position='soea',
            offset_x=offset_x,
            offset_y=offset_y,
            scale=scale,
        )

    @classmethod
    def repeat(
        cls,
        *,
        opacity: float,
        spacing_x: float | None = None,
        spacing_y: float | None = None,
        scale: float | None = None,
    ) -> Self:
        """Tile the watermark with optional horizontal and vertical spacing."""
        return cls(
            opacity=opacity,
            position='re',
            offset_x=spacing_x,
            offset_y=spacing_y,
            scale=scale,
        )

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
