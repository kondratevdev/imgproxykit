from dataclasses import dataclass
from typing import ClassVar, Self, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, kw_only=True)
class Padding(Option):
    """
    Add padding using CSS side order; specify at least one side.

    Uses CSS side order and is applied after image transformations,
    except watermarking. Padding follows DPR and uses the background color.
    Supply at least one side; omitted arguments remain
    ``None``.

    Use :meth:`all` for uniform padding, :meth:`symmetric` for separate
    horizontal and vertical padding, or the constructor for individual sides.

    Attributes:
        top: Top padding in pixels; fallback for omitted sides.
        right: Right padding; also used for an omitted left side.
        bottom: Bottom padding in pixels.
        left: Left padding in pixels.

    Usage:

    >>> option = Padding.all(10)
    >>> option.arguments
    (10, None, None, None)
    >>> option = Padding.symmetric(horizontal=20, vertical=10)
    >>> option.arguments
    (10, 20, None, None)
    >>> option = Padding(top=10, right=20, bottom=30, left=40)
    >>> option.arguments
    (10, 20, 30, 40)

    See `imgproxy padding
    <https://docs.imgproxy.net/usage/processing#padding>`_.

    """

    top: int | None = None
    right: int | None = None
    bottom: int | None = None
    left: int | None = None

    name: ClassVar[str] = 'padding'
    short_name: ClassVar[str | None] = 'pd'

    @classmethod
    def all(cls, value: int) -> Self:
        """Apply the same padding to all sides using protocol fallback."""
        return cls(top=value)

    @classmethod
    def symmetric(cls, *, horizontal: int, vertical: int) -> Self:
        """Set padding for both axes, requiring both values explicitly."""
        return cls(top=vertical, right=horizontal)

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.top, self.right, self.bottom, self.left)
