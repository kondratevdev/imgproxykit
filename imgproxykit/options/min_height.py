from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class MinHeight(ScalarOption[int]):
    """
    Set the minimum resulting height in pixels.

    Combining this option with a target height can crop the result.

    Attributes:
        value: Minimum resulting height in pixels.

    Usage:

    >>> option = MinHeight(200)
    >>> option.arguments
    (200,)

    See `imgproxy min height
    <https://docs.imgproxy.net/usage/processing#min-height>`_.
    """

    name: ClassVar[str] = 'min-height'
    short_name: ClassVar[str | None] = 'mh'
