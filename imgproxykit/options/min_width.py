from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class MinWidth(ScalarOption[int]):
    """
    Set the minimum resulting width in pixels.

    Combining this option with a target width can crop the result.

    Attributes:
        value: Minimum resulting width in pixels.

    Usage:

    >>> option = MinWidth(300)
    >>> option.arguments
    (300,)

    See `imgproxy min width
    <https://docs.imgproxy.net/usage/processing#min-width>`_.

    """

    name: ClassVar[str] = 'min-width'
    short_name: ClassVar[str | None] = 'mw'
