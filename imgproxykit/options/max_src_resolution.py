from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class MaxSrcResolution(ScalarOption[float]):
    """
    Override source megapixel limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    `IMGPROXY_ALLOW_SECURITY_OPTIONS
    <https://docs.imgproxy.net/latest/configuration/options#security>`__
    set to ``true`` on the imgproxy server.

    Attributes:
        value: Source resolution limit in megapixels.

    Usage:

    >>> option = MaxSrcResolution(50)
    >>> option.arguments
    (50,)

    See `imgproxy max src resolution
    <https://docs.imgproxy.net/usage/processing#max-src-resolution>`_.

    """

    name: ClassVar[OptionType] = 'max_src_resolution'
