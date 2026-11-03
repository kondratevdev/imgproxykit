from dataclasses import dataclass
from typing import ClassVar, Self, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True, kw_only=True)
class Trim(Option):
    """
    Trim the surrounding background with optional color and symmetry.

    Removes the surrounding background before resizing. Trimming loads
    the full image into memory and is unsupported for animated images.
    Omitted settings remain ``None``.

    Use :meth:`transparent` to trim transparent borders without specifying
    imgproxy's transparency key color.

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

    See `imgproxy trim <https://docs.imgproxy.net/usage/processing#trim>`_.
    """

    threshold: float
    color: str | None = None
    equal_hor: bool | None = None
    equal_ver: bool | None = None

    name: ClassVar[str] = 'trim'
    short_name: ClassVar[str | None] = 't'
    transparency_key: ClassVar[str] = 'FF00FF'

    @classmethod
    def transparent(
        cls,
        *,
        threshold: float,
        equal_hor: bool | None = None,
        equal_ver: bool | None = None,
    ) -> Self:
        """
        Trim transparent borders with optional symmetry on each axis.

        Uses imgproxy's magenta transparency key. Omitted symmetry flags
        remain ``None``; explicit ``False`` values are preserved.

        See `imgproxy trim <https://docs.imgproxy.net/usage/processing#trim>`_.
        """
        return cls(
            threshold=threshold,
            color=cls.transparency_key,
            equal_hor=equal_hor,
            equal_ver=equal_ver,
        )

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
