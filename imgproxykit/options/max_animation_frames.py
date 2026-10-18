from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class MaxAnimationFrames(Option):
    """
    Override animation frame limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    ``IMGPROXY_ALLOW_SECURITY_OPTIONS=true`` on the imgproxy server.

    Attributes:
        value: Maximum number of animation frames.

    Usage:

    >>> option = MaxAnimationFrames(100)
    >>> option.arguments
    (100,)

    See `imgproxy max animation frames
    <https://docs.imgproxy.net/usage/processing#max-animation-frames>`_.

    """

    value: int

    _name: ClassVar[OptionType] = 'maf'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
