from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class EnforceThumbnail(ScalarOption[bool]):
    """
    Use an embedded HEIC or AVIF thumbnail when available.

    Uses the embedded thumbnail instead of the main source image
    when available. Supported for HEIC and AVIF sources.

    Attributes:
        value: Whether to prefer an embedded thumbnail.

    Usage:

    >>> option = EnforceThumbnail(True)
    >>> option.arguments
    (True,)

    See `imgproxy enforce thumbnail
    <https://docs.imgproxy.net/usage/processing#enforce-thumbnail>`_.

    """

    name: ClassVar[OptionType] = 'enforce_thumbnail'
