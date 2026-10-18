from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class StripMetadata(Option):
    """
    Remove image metadata.

    Overrides the server metadata stripping setting for this request.

    Attributes:
        value: Whether to remove EXIF, IPTC, and other image metadata.

    Usage:

    >>> option = StripMetadata(True)
    >>> option.arguments
    (True,)

    See `imgproxy strip metadata
    <https://docs.imgproxy.net/usage/processing#strip-metadata>`_.

    """

    value: bool

    _name: ClassVar[OptionType] = 'sm'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
