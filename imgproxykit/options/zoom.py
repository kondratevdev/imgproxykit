import math
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

    Raises:
        ValueError: If ``factor_x`` or ``factor_y`` is not a finite number
            greater than zero.

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

    @override
    def validate(self) -> None:
        """
        Validate that zoom factors are finite and greater than zero.

        Raises:
            ValueError: If ``factor_x`` or ``factor_y`` is less than or
                equal to zero, infinite, or NaN.

        """
        if isinstance(self.factor_x, bool) or not (
            math.isfinite(self.factor_x) and self.factor_x > 0
        ):
            raise ValueError(
                'Zoom factor_x must be greater than zero, '
                f'got {self.factor_x}.',
            )
        if self.factor_y is not None and (
            isinstance(self.factor_y, bool)
            or not (math.isfinite(self.factor_y) and self.factor_y > 0)
        ):
            raise ValueError(
                'Zoom factor_y must be greater than zero, '
                f'got {self.factor_y}.',
            )

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.factor_x, self.factor_y)
