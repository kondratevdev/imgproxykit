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
        ValueError: If the value is not a finite number greater than zero.

    Usage:

    >>> option = DPR(2)
    >>> option.arguments
    (2,)

    See `imgproxy DPR
    <https://docs.imgproxy.net/usage/processing#dpr>`_.
    """

    # Public API:

    # Public API:
    name: ClassVar[str] = 'dpr'

    @override
    def validate(self) -> None:
        """Require a finite multiplier greater than zero."""
        if not (math.isfinite(self.value) and self.value > 0):
            raise ValueError(
                f'DPR must be a finite number greater than zero, '
                f'got {self.value!r}',
            )
