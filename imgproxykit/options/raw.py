from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class Raw(ScalarOption[bool]):
    """
    Stream the unchecked source file without processing.

    Streams the source without checking its type, resolution, or size.
    The output is not transformed.

    Attributes:
        value: Whether to stream the raw source file.

    Usage:

    >>> option = Raw(True)
    >>> option.arguments
    (True,)

    See `imgproxy raw
    <https://docs.imgproxy.net/usage/processing#raw>`_.

    """

    name: ClassVar[OptionType] = 'raw'
