from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class StripColorProfile(Option):
    """
    Convert the embedded profile to sRGB and remove it.

    When enabled, imgproxy converts the embedded ICC profile to sRGB
    and removes it. Otherwise, imgproxy tries to preserve the profile.

    Attributes:
        value: Whether to convert and remove the embedded color profile.

    Usage:

    >>> option = StripColorProfile(True)
    >>> option.arguments
    (True,)

    See `imgproxy strip color profile
    <https://docs.imgproxy.net/usage/processing#strip-color-profile>`_.

    """

    value: bool

    name: ClassVar[OptionType] = 'strip_color_profile'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
