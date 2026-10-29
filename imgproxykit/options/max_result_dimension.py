from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class MaxResultDimension(ScalarOption[int]):
    """
    Override output dimension limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    `IMGPROXY_ALLOW_SECURITY_OPTIONS
    <https://docs.imgproxy.net/latest/configuration/options#security>`__
    set to ``true`` on the imgproxy server.

    Attributes:
        value: Maximum resulting width or height in pixels.

    Usage:

    >>> option = MaxResultDimension(4096)
    >>> option.arguments
    (4096,)

    See `imgproxy max result dimension
    <https://docs.imgproxy.net/usage/processing#max-result-dimension>`_.

    """

    name: ClassVar[str] = 'max_result_dimension'
    short_name: ClassVar[str | None] = 'mrd'
