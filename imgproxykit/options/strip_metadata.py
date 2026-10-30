from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class StripMetadata(ScalarOption[bool]):
    """
    Remove image metadata.

    Overrides the server metadata stripping setting for this request.

    Attributes:
        value: Whether to remove EXIF, IPTC, and other image metadata.

    Usage:

    >>> option = StripMetadata(True)
    >>> option.arguments
    (True,)

    See `imgproxy strip metadata
    <https://docs.imgproxy.net/usage/processing#strip-metadata>`_.
    """

    name: ClassVar[str] = 'strip_metadata'
    short_name: ClassVar[str | None] = 'sm'
