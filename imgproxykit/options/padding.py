from dataclasses import dataclass
from typing import ClassVar, override

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

    Attributes:
        top: Top padding in pixels; fallback for omitted sides.
        right: Right padding; also used for an omitted left side.
        bottom: Bottom padding in pixels.
        left: Left padding in pixels.

    Usage:

    >>> option = Padding(top=10)
    >>> option.arguments
    (10, None, None, None)
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

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.top, self.right, self.bottom, self.left)
