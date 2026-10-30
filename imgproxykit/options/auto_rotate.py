from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class AutoRotate(ScalarOption[bool]):
    """
    Apply the source EXIF orientation before processing.

    Overrides automatic EXIF orientation handling for this request.
    The orientation tag is removed regardless of this setting.

    Attributes:
        value: Whether to apply the source EXIF orientation.

    Usage:

    >>> option = AutoRotate(False)
    >>> option.arguments
    (False,)

    See `imgproxy auto rotate
    <https://docs.imgproxy.net/usage/processing#auto-rotate>`_.
    """

    name: ClassVar[str] = 'auto_rotate'
    short_name: ClassVar[str | None] = 'ar'
