from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class DPR(Option):
    """
    Scale an image for high pixel density displays.

    The factor also scales gravity offsets, watermark offsets, and padding.

    Attributes:
        value: Positive pixel density multiplier.

    Usage:

    >>> option = DPR(2)
    >>> option.arguments
    (2,)

    See `imgproxy DPR
    <https://docs.imgproxy.net/usage/processing#dpr>`_.

    """

    # Public API:
    value: float

    # Public API:
    name: ClassVar[OptionType] = 'dpr'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
