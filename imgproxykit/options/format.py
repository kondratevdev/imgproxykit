from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, FormatType, OptionType


@final
@dataclass(frozen=True, slots=True)
class Format(Option):
    """
    Set the output image format.

    Attributes:
        value: Output format, such as ``webp`` or ``avif``.

    Usage:

    >>> option = Format('webp')
    >>> option.arguments
    ('webp',)

    See `imgproxy format
    <https://docs.imgproxy.net/usage/processing#format>`_.

    """

    # Public API:
    value: FormatType

    # Private API:
    _name: ClassVar[OptionType] = 'f'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
