from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Rotate(ScalarOption[int]):
    """
    Rotate clockwise by a multiple of 90 degrees.

    Rotation follows EXIF orientation unless automatic rotation is disabled.

    Attributes:
        value: Clockwise angle in degrees; must be a multiple of 90.

    Raises:
        ValueError: If ``value`` is not an integer multiple of 90.

    Usage:

    >>> option = Rotate(90)
    >>> option.arguments
    (90,)

    See `imgproxy rotate
    <https://docs.imgproxy.net/usage/processing#rotate>`_.

    """

    name: ClassVar[str] = 'rotate'
    short_name: ClassVar[str | None] = 'rot'

    @override
    def validate(self) -> None:
        """
        Validate that the angle is an integer multiple of 90 degrees.

        Raises:
            ValueError: If angle is not a multiple of 90 or is a boolean.

        """
        if isinstance(self.value, bool) or not (
            isinstance(self.value, int) and self.value % 90 == 0
        ):
            msg = f'Angle must be an integer multiple of 90, got {self.value}.'
            raise ValueError(msg)
