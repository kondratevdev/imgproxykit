from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, ExtendGravityType

if TYPE_CHECKING:
    from imgproxykit.options.gravity import Gravity


@dataclass(frozen=True, slots=True, kw_only=True)
class ExtendAspectRatio(Option):
    """
    Extend the canvas to the requested aspect ratio.

    Omitted settings remain ``None``. The default
    anchor is center without offsets; smart gravity is unsupported.

    Attributes:
        value: Whether canvas extension is enabled.
        gravity: Canvas anchor and offsets supplied as a Gravity option.
            Smart gravity is unsupported.

    Usage:

    >>> from imgproxykit.options import Gravity
    >>> option = ExtendAspectRatio(value=True, gravity=Gravity.bottom())
    >>> option.arguments
    (True, 'so', None, None)

    See `imgproxy extend aspect ratio
    <https://docs.imgproxy.net/usage/processing#extend-aspect-ratio>`_.
    """

    value: bool
    gravity: 'Gravity[ExtendGravityType] | None' = None

    name: ClassVar[str] = 'extend_aspect_ratio'
    short_name: ClassVar[str | None] = 'exar'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.value,
            *(
                # Gravity type, horizontal offset, vertical offset.
                (None, None, None)
                if self.gravity is None
                else self.gravity.arguments
            ),
        )
