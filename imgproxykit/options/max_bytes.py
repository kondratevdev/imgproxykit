from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class MaxBytes(ScalarOption[int]):
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

    name: ClassVar[OptionType] = 'max_bytes'
