import math
from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class DPR(ScalarOption[float]):
    """
    Scale an image for high pixel density displays.

    The factor also scales gravity offsets, watermark offsets, and padding.

    Attributes:
        value: Positive pixel density multiplier.

    Raises:
        ValueError: If ``value`` is not a finite number greater than zero.

    Usage:

    >>> option = DPR(2)
    >>> option.arguments
    (2,)

    See `imgproxy DPR
    <https://docs.imgproxy.net/usage/processing#dpr>`_.

    """

    # Public API:
    name: ClassVar[str] = 'dpr'

    @override
    def validate(self) -> None:
        """
        Validate that the DPR factor is finite and greater than zero.

        Raises:
            ValueError: If the factor is less than or equal to zero,
                infinite, or NaN.

        """
        if isinstance(self.value, bool) or not (
            math.isfinite(self.value) and self.value > 0
        ):
            raise ValueError(
                f'DPR factor must be greater than zero, got {self.value}.',
            )
