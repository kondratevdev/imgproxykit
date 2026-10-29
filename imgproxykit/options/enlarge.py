from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Enlarge(ScalarOption[bool]):
    """
    Allow upscaling smaller source images.

    Allows imgproxy to upscale sources smaller than the target dimensions.

    Attributes:
        value: Whether smaller source images may be enlarged.

    Usage:

    >>> option = Enlarge(True)
    >>> option.arguments
    (True,)

    See `imgproxy enlarge
    <https://docs.imgproxy.net/usage/processing#enlarge>`_.

    """

    name: ClassVar[str] = 'enlarge'
    short_name: ClassVar[str | None] = 'el'
