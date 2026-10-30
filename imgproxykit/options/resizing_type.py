from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import ResizeType


@dataclass(frozen=True, slots=True)
class ResizingType(ScalarOption[ResizeType]):
    """
    Choose the resizing strategy.

    Controls how target dimensions and the source aspect ratio interact.

    Attributes:
        value: Resizing strategy: ``fit``, ``fill``, ``fill-down``,
            ``force``, or ``auto``.

    Usage:

    >>> option = ResizingType('fill')
    >>> option.arguments
    ('fill',)

    See `imgproxy resizing type
    <https://docs.imgproxy.net/usage/processing#resizing-type>`_.
    """

    name: ClassVar[str] = 'resizing_type'
    short_name: ClassVar[str | None] = 'rt'
