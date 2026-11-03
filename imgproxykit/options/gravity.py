from dataclasses import dataclass
from typing import ClassVar, Generic, Literal, final, override

from typing_extensions import TypeVar

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, GravityType

_GravityT_co = TypeVar(
    '_GravityT_co',
    bound=GravityType,
    covariant=True,
    default=GravityType,
)


# NOTE: For now, keep one generic class with static factories so each factory
# returns an exact position type and Extend options can exclude smart gravity.
# Factories construct Gravity directly, so subclassing is disabled for now.
@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Gravity(Option, Generic[_GravityT_co]):  # noqa: WPS214
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

    position: _GravityT_co
    offset_x: float | None = None
    offset_y: float | None = None

    name: ClassVar[str] = 'gravity'
    short_name: ClassVar[str | None] = 'g'

    # Static factories preserve the exact position independently of the class.
    @staticmethod
    def center(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["ce"]]':
        """Anchor cropping to the center with optional offsets."""
        return Gravity(position='ce', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def top(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["no"]]':
        """Anchor cropping to the top edge with optional offsets."""
        return Gravity(position='no', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def bottom(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["so"]]':
        """Anchor cropping to the bottom edge with optional offsets."""
        return Gravity(position='so', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def left(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["we"]]':
        """Anchor cropping to the left edge with optional offsets."""
        return Gravity(position='we', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def right(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["ea"]]':
        """Anchor cropping to the right edge with optional offsets."""
        return Gravity(position='ea', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def top_left(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["nowe"]]':
        """Anchor cropping to the top-left corner with optional offsets."""
        return Gravity(position='nowe', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def top_right(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["noea"]]':
        """Anchor cropping to the top-right corner with optional offsets."""
        return Gravity(position='noea', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def bottom_left(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["sowe"]]':
        """Anchor cropping to the bottom-left corner with optional offsets."""
        return Gravity(position='sowe', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def bottom_right(
        *,
        offset_x: float | None = None,
        offset_y: float | None = None,
    ) -> 'Gravity[Literal["soea"]]':
        """Anchor cropping to the bottom-right corner with optional offsets."""
        return Gravity(position='soea', offset_x=offset_x, offset_y=offset_y)

    @staticmethod
    def smart() -> 'Gravity[Literal["sm"]]':
        """Let imgproxy select the most interesting image area."""
        return Gravity(position='sm')

    @staticmethod
    def focus(*, x: float, y: float) -> 'Gravity[Literal["fp"]]':  # noqa: WPS111
        """Center cropping on focus coordinates in the range [0, 1]."""
        return Gravity(position='fp', offset_x=x, offset_y=y)

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.position, self.offset_x, self.offset_y)
