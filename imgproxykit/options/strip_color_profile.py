from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class StripColorProfile(ScalarOption[bool]):
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

    name: ClassVar[str] = 'strip_color_profile'
    short_name: ClassVar[str | None] = 'scp'
