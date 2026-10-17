from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Preset(Option):
    """
    Reference named presets configured on the imgproxy server.

    Names retain their supplied order. Multiple Preset instances remain
    separate options, preserving their positions among other options.
    Preset definitions are resolved by the server, not expanded locally.

    Attributes:
        names: Ordered names of server presets to apply.

    Usage:

    >>> option = Preset(names=('thumbnail', 'watermarked'))
    >>> option.arguments
    ('thumbnail', 'watermarked')

    See `imgproxy preset
    <https://docs.imgproxy.net/usage/processing#preset>`_.

    """

    names: tuple[str, ...]

    _name: ClassVar[OptionType] = 'pr'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Preset names in imgproxy protocol order."""
        return self.names
