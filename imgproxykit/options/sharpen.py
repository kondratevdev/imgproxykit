from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Sharpen(ScalarOption[float]):
    """
    Apply sharpening with the given sigma.

    The sigma controls the size of the sharpening mask.

    Attributes:
        value: Sharpening filter sigma.

    Usage:

    >>> option = Sharpen(1.0)
    >>> option.arguments
    (1.0,)

    See `imgproxy sharpen
    <https://docs.imgproxy.net/usage/processing#sharpen>`_.
    """

    name: ClassVar[str] = 'sharpen'
    short_name: ClassVar[str | None] = 'sh'
