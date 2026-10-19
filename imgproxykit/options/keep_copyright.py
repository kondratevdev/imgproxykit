from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class KeepCopyright(Option):
    """
    Preserve copyright information when stripping metadata.

    Applies when metadata is being stripped from the output image.

    Attributes:
        value: Whether to retain copyright metadata.

    Usage:

    >>> option = KeepCopyright(True)
    >>> option.arguments
    (True,)

    See `imgproxy keep copyright
    <https://docs.imgproxy.net/usage/processing#keep-copyright>`_.

    """

    value: bool

    name: ClassVar[OptionType] = 'keep_copyright'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
