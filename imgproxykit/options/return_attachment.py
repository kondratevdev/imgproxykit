from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class ReturnAttachment(Option):
    """
    Request attachment disposition for downloading.

    Sets attachment disposition so browsers can offer to save the image.
    Combine with Filename to choose the downloaded filename.

    Attributes:
        value: Whether to return an attachment disposition.

    Usage:

    >>> option = ReturnAttachment(True)
    >>> option.arguments
    (True,)

    See `imgproxy return attachment
    <https://docs.imgproxy.net/usage/processing#return-attachment>`_.

    """

    value: bool

    _name: ClassVar[OptionType] = 'att'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
