from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class DPR(ScalarOption[float]):
    """
    Scale an image for high pixel density displays.

    The factor also scales gravity offsets, watermark offsets, and padding.

    Attributes:
        value: Positive pixel density multiplier.

    Usage:

    >>> option = DPR(2)
    >>> option.arguments
    (2,)

    See `imgproxy DPR
    <https://docs.imgproxy.net/usage/processing#dpr>`_.
    """

    # Public API:

    # Public API:
    name: ClassVar[str] = 'dpr'
