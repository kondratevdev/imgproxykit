from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, kw_only=True)
class Zoom(Option):
    """
    Multiply dimensions by one factor or separate X and Y factors.

    Unlike DPR, zoom does not scale gravity offsets, watermark offsets,
    or padding. Factors must be greater than zero.

    Attributes:
        factor_x: Horizontal multiplier, also used vertically when
            ``factor_y`` is omitted.
        factor_y: Optional vertical multiplier.

    Usage:

    >>> option = Zoom(factor_x=2)
    >>> option.arguments
    (2, None)
    >>> option = Zoom(factor_x=2, factor_y=1.5)
    >>> option.arguments
    (2, 1.5)

    See `imgproxy zoom
    <https://docs.imgproxy.net/usage/processing#zoom>`_.

    """

    factor_x: float
    factor_y: float | None = None

    name: ClassVar[str] = 'zoom'
    short_name: ClassVar[str | None] = 'z'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.factor_x, self.factor_y)
