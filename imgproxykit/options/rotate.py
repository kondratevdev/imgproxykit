from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Rotate(ScalarOption[int]):
    """
    Rotate clockwise by a multiple of 90 degrees.

    Rotation follows EXIF orientation unless automatic rotation is disabled.

    Attributes:
        value: Clockwise angle in degrees; must be a multiple of 90.

    Usage:

    >>> option = Rotate(90)
    >>> option.arguments
    (90,)

    See `imgproxy rotate
    <https://docs.imgproxy.net/usage/processing#rotate>`_.
    """

    name: ClassVar[str] = 'rotate'
    short_name: ClassVar[str | None] = 'rot'
