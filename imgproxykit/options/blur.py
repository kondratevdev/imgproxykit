from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class Blur(ScalarOption[float]):
    """
    Apply Gaussian blur with the given sigma.

    The sigma controls the size of the Gaussian blur mask.

    Attributes:
        value: Gaussian blur sigma.

    Usage:

    >>> option = Blur(2.0)
    >>> option.arguments
    (2.0,)

    See `imgproxy blur
    <https://docs.imgproxy.net/usage/processing#blur>`_.

    """

    name: ClassVar[OptionType] = 'blur'
