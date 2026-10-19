from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class Expires(ScalarOption[int]):
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

    name: ClassVar[OptionType] = 'expires'
