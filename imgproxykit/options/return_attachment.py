from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class ReturnAttachment(ScalarOption[bool]):
    """
    Request attachment disposition for downloading.

    Sets attachment disposition so browsers can offer to save the image.
    Combine with Filename to choose the downloaded filename.

    Attributes:
        value: Whether to return an attachment disposition.

    Usage:

    >>> option = ReturnAttachment(True)
    >>> option.arguments
    (True,)

    See `imgproxy return attachment
    <https://docs.imgproxy.net/usage/processing#return-attachment>`_.

    """

    name: ClassVar[OptionType] = 'return_attachment'
