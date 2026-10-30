from dataclasses import dataclass
from typing import ClassVar, Self, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, Position


@dataclass(frozen=True, slots=True, kw_only=True)
class Gravity(Option):  # noqa: WPS214
    """
    Choose the image area retained when cropping.

    Use readable anchor factories, :meth:`smart`, or :meth:`focus`.
    The constructor also accepts imgproxy position codes directly.
    Omitted offsets remain ``None``.

    Attributes:
        position: Anchor such as ``ce`` (center), ``sm`` (smart),
            or ``fp`` (focus point).
        offset_x: Horizontal offset; with ``fp``, the focus X coordinate.
        offset_y: Vertical offset; with ``fp``, the focus Y coordinate.

    Usage:

    >>> option = Gravity.center()
    >>> option.arguments
    ('ce', None, None)
    >>> option = Gravity.focus(x=0.25, y=0.5)
    >>> option.arguments
    ('fp', 0.25, 0.5)

    See `imgproxy gravity
    <https://docs.imgproxy.net/usage/processing#gravity>`_.
    """

    position: Position
    offset_x: float | None = None
    offset_y: float | None = None

    name: ClassVar[str] = 'gravity'
    short_name: ClassVar[str | None] = 'g'

    @classmethod
    def center(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the center with optional offsets."""
        return cls(position='ce', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def top(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the top edge with optional offsets."""
        return cls(position='no', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def bottom(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the bottom edge with optional offsets."""
        return cls(position='so', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def left(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the left edge with optional offsets."""
        return cls(position='we', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def right(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the right edge with optional offsets."""
        return cls(position='ea', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def top_left(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the top-left corner with optional offsets."""
        return cls(position='nowe', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def top_right(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the top-right corner with optional offsets."""
        return cls(position='noea', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def bottom_left(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the bottom-left corner with optional offsets."""
        return cls(position='sowe', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def bottom_right(
        cls,
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> Self:
        """Anchor cropping to the bottom-right corner with optional offsets."""
        return cls(position='soea', offset_x=offset_x, offset_y=offset_y)

    @classmethod
    def smart(cls) -> Self:
        """Let imgproxy select the most interesting image area."""
        return cls(position='sm')

    @classmethod
    def focus(cls, *, x: float, y: float) -> Self:  # noqa: WPS111
        """Center cropping on focus coordinates in the range [0, 1]."""
        return cls(position='fp', offset_x=x, offset_y=y)

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.position, self.offset_x, self.offset_y)
