from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@dataclass(frozen=True, slots=True, kw_only=True)
class Trim(Option):
    """
    Trim the surrounding background with optional color and symmetry.

    Removes the surrounding background before resizing. Trimming loads
    the full image into memory and is unsupported for animated images.
    Omitted settings remain :data:`~imgproxykit.types.EMPTY`.

    Attributes:
        threshold: Color similarity tolerance.
        color: Optional hex background color; ``FF00FF`` selects
            transparent backgrounds. Omission enables automatic detection.
        equal_hor: Trim equal amounts from the left and right sides.
        equal_ver: Trim equal amounts from the top and bottom sides.

    Usage:

    >>> option = Trim(threshold=10, color='ffffff', equal_hor=True)
    >>> option.arguments
    (10, 'ffffff', True, EMPTY)

    See `imgproxy trim
    <https://docs.imgproxy.net/usage/processing#trim>`_.

    """

    threshold: float
    color: str | EMPTY = EMPTY
    equal_hor: bool | EMPTY = EMPTY
    equal_ver: bool | EMPTY = EMPTY

    name: ClassVar[OptionType] = 'trim'

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
