from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class MaxAnimationFrameResolution(Option):
    """
    Override frame megapixel limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    ``IMGPROXY_ALLOW_SECURITY_OPTIONS=true`` on the imgproxy server.

    Attributes:
        value: Animation frame resolution limit in megapixels.

    Usage:

    >>> option = MaxAnimationFrameResolution(20)
    >>> option.arguments
    (20,)

    See `imgproxy max animation frame resolution
    <https://docs.imgproxy.net/usage/processing#max-animation-frame-resolution>`_.

    """

    value: float

    _name: ClassVar[OptionType] = 'mafr'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
