from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class Enlarge(Option):
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

    value: bool

    name: ClassVar[OptionType] = 'enlarge'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
