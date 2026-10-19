from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class Quality(ScalarOption[int]):
    """
    Set output image quality.

    Attributes:
        value: Quality percentage. Zero delegates to server quality settings.

    Usage:

    >>> option = Quality(85)
    >>> option.arguments
    (85,)

    See `imgproxy quality
    <https://docs.imgproxy.net/usage/processing#quality>`_.

    """

    # Public API:

    # Public API:
    name: ClassVar[OptionType] = 'quality'
