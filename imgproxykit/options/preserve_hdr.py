from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class PreserveHDR(Option):
    """
    Preserve high bit depth instead of converting to 8 bit.

    Overrides the server high bit depth setting for this request.

    Attributes:
        value: Whether to retain high bit depth instead of using 8 bit.

    Usage:

    >>> option = PreserveHDR(True)
    >>> option.arguments
    (True,)

    See `imgproxy preserve hdr
    <https://docs.imgproxy.net/usage/processing#preserve-hdr>`_.

    """

    value: bool

    name: ClassVar[OptionType] = 'preserve_hdr'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
