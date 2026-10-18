from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class MaxBytes(Option):
    """
    Reduce output quality to meet the requested byte limit.

    imgproxy may encode the image repeatedly to reduce its quality.
    Applicable to JPEG, WebP, HEIC, and TIFF output.

    Attributes:
        value: Maximum requested output size in bytes; zero disables it.

    Usage:

    >>> option = MaxBytes(100_000)
    >>> option.arguments
    (100000,)

    See `imgproxy max bytes
    <https://docs.imgproxy.net/usage/processing#max-bytes>`_.

    """

    value: int

    _name: ClassVar[OptionType] = 'mb'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
