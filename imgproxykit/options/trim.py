from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, kw_only=True)
class Trim(Option):
    """
    Trim the surrounding background with optional color and symmetry.

    Removes the surrounding background before resizing. Trimming loads
    the full image into memory and is unsupported for animated images.
    Omitted settings remain ``None``.

    Attributes:
        threshold: Color similarity tolerance.
        color: Optional hex background color; ``FF00FF`` selects
            transparent backgrounds. Omission enables automatic detection.
        equal_hor: Trim equal amounts from the left and right sides.
        equal_ver: Trim equal amounts from the top and bottom sides.

    Usage:

    >>> option = Trim(threshold=10, color='ffffff', equal_hor=True)
    >>> option.arguments
    (10, 'ffffff', True, None)

    See `imgproxy trim
    <https://docs.imgproxy.net/usage/processing#trim>`_.

    """

    threshold: float
    color: str | None = None
    equal_hor: bool | None = None
    equal_ver: bool | None = None

    name: ClassVar[str] = 'trim'
    short_name: ClassVar[str | None] = 't'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.threshold,
            self.color,
            self.equal_hor,
            self.equal_ver,
        )
