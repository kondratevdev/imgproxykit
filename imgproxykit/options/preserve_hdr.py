from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class PreserveHDR(ScalarOption[bool]):
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

    name: ClassVar[OptionType] = 'preserve_hdr'
