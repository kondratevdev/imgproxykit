from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Width(ScalarOption[int]):
    """
    Set the target width in pixels.

    Zero lets imgproxy calculate width from height and aspect ratio.
    With force resizing, zero preserves the source width.

    Attributes:
        value: Target width in pixels.

    Usage:

    >>> option = Width(300)
    >>> option.arguments
    (300,)

    See `imgproxy width
    <https://docs.imgproxy.net/usage/processing#width>`_.
    """

    name: ClassVar[str] = 'width'
    short_name: ClassVar[str | None] = 'w'
