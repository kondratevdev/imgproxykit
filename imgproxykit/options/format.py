from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import FormatType


@dataclass(frozen=True, slots=True)
class Format(ScalarOption[FormatType]):
    """
    Set the output image format.

    Attributes:
        value: Output format, such as ``webp`` or ``avif``.

    Usage:

    >>> option = Format('webp')
    >>> option.arguments
    ('webp',)

    See `imgproxy format
    <https://docs.imgproxy.net/usage/processing#format>`_.

    """

    # Public API:

    # Public API:
    name: ClassVar[str] = 'format'
    short_name: ClassVar[str | None] = 'f'
