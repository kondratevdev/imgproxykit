from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class MaxSrcFileSize(Option):
    """
    Override source byte limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    ``IMGPROXY_ALLOW_SECURITY_OPTIONS=true`` on the imgproxy server.

    Attributes:
        value: Source file size limit in bytes.

    Usage:

    >>> option = MaxSrcFileSize(10_000_000)
    >>> option.arguments
    (10000000,)

    See `imgproxy max src file size
    <https://docs.imgproxy.net/usage/processing#max-src-file-size>`_.

    """

    value: int

    _name: ClassVar[OptionType] = 'msfs'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
