from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


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

    name: ClassVar[str] = 'quality'
    short_name: ClassVar[str | None] = 'q'
