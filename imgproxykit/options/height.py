from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Height(ScalarOption[int]):
    """
    Set the target height in pixels.

    Zero lets imgproxy calculate height from width and aspect ratio.
    With force resizing, zero preserves the source height.

    Attributes:
        value: Target height in pixels.

    Usage:

    >>> option = Height(200)
    >>> option.arguments
    (200,)

    See `imgproxy height
    <https://docs.imgproxy.net/usage/processing#height>`_.
    """

    name: ClassVar[str] = 'height'
    short_name: ClassVar[str | None] = 'h'
