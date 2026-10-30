import re
from dataclasses import dataclass
from typing import ClassVar, Final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument

# Characters a URL path segment carries literally (RFC 3986 ``pchar``
# without percent-encoding). imgproxy matches preset names as written in
# the path and does not decode them, so other characters cannot be used.
_NAME_PATTERN: Final = re.compile(r"[A-Za-z0-9\-._~!$&'()*+,;=:@]+")


@dataclass(frozen=True, slots=True, init=False)
class Preset(Option):
    """
    Reference named presets configured on the imgproxy server.

    Names retain their supplied order. Multiple Preset instances remain
    separate options, preserving their positions among other options.
    Preset definitions are resolved by the server, not expanded locally.

    Names must be non-empty and use only ASCII letters, digits, and
    ``-._~!$&'()*+,;=:@``. Characters such as ``/``, ``?``, ``#``, ``%``,
    spaces, and non-ASCII letters would change the URL structure or never
    match a server preset. The configured arguments separator is rejected
    when the URL is built.

    Raises:
        ValueError: If a name is empty or contains an unsupported character.

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

    @override
    def validate(self) -> None:
        """Require names that imgproxy can match exactly."""
        for preset_name in self.names:
            if not _NAME_PATTERN.fullmatch(preset_name):
                raise ValueError(
                    'Preset names must be non-empty and use only ASCII '
                    "letters, digits, and -._~!$&'()*+,;=:@, "
                    f'got {preset_name!r}',
                )
