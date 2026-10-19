from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class KeepCopyright(ScalarOption[bool]):
    """
    Preserve copyright information when stripping metadata.

    Applies when metadata is being stripped from the output image.

    Attributes:
        value: Whether to retain copyright metadata.

    Usage:

    >>> option = KeepCopyright(True)
    >>> option.arguments
    (True,)

    See `imgproxy keep copyright
    <https://docs.imgproxy.net/usage/processing#keep-copyright>`_.

    """

    name: ClassVar[OptionType] = 'keep_copyright'
