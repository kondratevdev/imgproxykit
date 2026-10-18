from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class AutoRotate(Option):
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

    value: bool

    _name: ClassVar[OptionType] = 'ar'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
