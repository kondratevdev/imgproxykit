from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType, ResizeType


@final
@dataclass(frozen=True, slots=True)
class ResizingType(Option):
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

    value: ResizeType

    _name: ClassVar[OptionType] = 'rt'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
