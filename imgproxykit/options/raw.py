from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class Raw(Option):
    """
    Stream the unchecked source file without processing.

    Streams the source without checking its type, resolution, or size.
    The output is not transformed.

    Attributes:
        value: Whether to stream the raw source file.

    Usage:

    >>> option = Raw(True)
    >>> option.arguments
    (True,)

    See `imgproxy raw
    <https://docs.imgproxy.net/usage/processing#raw>`_.

    """

    value: bool

    name: ClassVar[OptionType] = 'raw'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
