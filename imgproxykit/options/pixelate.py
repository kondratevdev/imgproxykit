from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Pixelate(ScalarOption[int]):
    """
    Set the pixelation block size.

    Larger blocks produce a coarser pixelation effect.

    Attributes:
        value: Individual pixel block size in pixels.

    Usage:

    >>> option = Pixelate(10)
    >>> option.arguments
    (10,)

    See `imgproxy pixelate
    <https://docs.imgproxy.net/usage/processing#pixelate>`_.

    """

    name: ClassVar[str] = 'pixelate'
    short_name: ClassVar[str | None] = 'pix'
