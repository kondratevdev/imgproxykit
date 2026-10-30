from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, init=False)
class Preset(Option):
    """
    Reference named presets configured on the imgproxy server.

    Names retain their supplied order. Multiple Preset instances remain
    separate options, preserving their positions among other options.
    Preset definitions are resolved by the server, not expanded locally.

    Attributes:
        names: Ordered names of server presets to apply.

    Usage:

    >>> option = Preset('thumbnail', 'watermarked')
    >>> option.arguments
    ('thumbnail', 'watermarked')

    See `imgproxy preset
    <https://docs.imgproxy.net/usage/processing#preset>`_.
    """

    names: tuple[str, ...]

    name: ClassVar[str] = 'preset'
    short_name: ClassVar[str | None] = 'pr'

    def __init__(self, *names: str) -> None:
        """
        Store preset names in their supplied order.

        Args:
            *names: Server preset names in imgproxy protocol order.

        Examples:
            Reference a single preset, then several in order:

            >>> Preset('thumbnail').arguments
            ('thumbnail',)
            >>> Preset('thumbnail', 'watermarked').arguments
            ('thumbnail', 'watermarked')

        """
        # Keep variadic names while initializing a frozen dataclass.
        # Bypassing __setattr__ is safe until initialization is finished.
        object.__setattr__(self, 'names', names)
        self.validate()

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Preset names in imgproxy protocol order."""
        return self.names
