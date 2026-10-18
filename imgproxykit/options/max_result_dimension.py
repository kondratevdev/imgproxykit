from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class MaxResultDimension(Option):
    """
    Override output dimension limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    ``IMGPROXY_ALLOW_SECURITY_OPTIONS=true`` on the imgproxy server.

    Attributes:
        value: Maximum resulting width or height in pixels.

    Usage:

    >>> option = MaxResultDimension(4096)
    >>> option.arguments
    (4096,)

    See `imgproxy max result dimension
    <https://docs.imgproxy.net/usage/processing#max-result-dimension>`_.

    """

    value: int

    _name: ClassVar[OptionType] = 'mrd'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
