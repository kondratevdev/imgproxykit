from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class MaxSrcResolution(Option):
    """
    Override source megapixel limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    ``IMGPROXY_ALLOW_SECURITY_OPTIONS=true`` on the imgproxy server.

    Attributes:
        value: Source resolution limit in megapixels.

    Usage:

    >>> option = MaxSrcResolution(50)
    >>> option.arguments
    (50,)

    See `imgproxy max src resolution
    <https://docs.imgproxy.net/usage/processing#max-src-resolution>`_.

    """

    value: float

    _name: ClassVar[OptionType] = 'msr'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
