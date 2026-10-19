from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class Expires(Option):
    """
    Reject the URL after the given Unix timestamp.

    imgproxy returns HTTP 404 after the supplied timestamp has expired.

    Attributes:
        value: Expiration time as a Unix timestamp in seconds.

    Usage:

    >>> option = Expires(300)
    >>> option.arguments
    (300,)

    See `imgproxy expires
    <https://docs.imgproxy.net/usage/processing#expires>`_.

    """

    value: int

    name: ClassVar[OptionType] = 'expires'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
