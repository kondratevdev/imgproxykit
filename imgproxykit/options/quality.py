from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Quality(ScalarOption[int]):
    """
    Set output image quality.

    Attributes:
        value: Quality percentage. Zero delegates to server quality settings.

    Raises:
        ValueError: If ``value`` is not an integer between 0 and 100.

    Usage:

    >>> option = Quality(85)
    >>> option.arguments
    (85,)

    See `imgproxy quality
    <https://docs.imgproxy.net/usage/processing#quality>`_.

    """

    # Public API:
    name: ClassVar[str] = 'quality'
    short_name: ClassVar[str | None] = 'q'

    @override
    def validate(self) -> None:
        """
        Validate that the quality percentage is between 0 and 100.

        Raises:
            ValueError: If quality is outside 0..100 or is a boolean.

        """
        if isinstance(self.value, bool) or not (
            isinstance(self.value, int) and 0 <= self.value <= 100
        ):
            msg = (
                f'Quality must be an integer between 0 and 100, '
                f'got {self.value}.'
            )
            raise ValueError(msg)
