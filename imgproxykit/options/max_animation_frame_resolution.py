from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class MaxAnimationFrameResolution(ScalarOption[float]):
    """
    Override frame megapixel limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    `IMGPROXY_ALLOW_SECURITY_OPTIONS
    <https://docs.imgproxy.net/latest/configuration/options#security>`__
    set to ``true`` on the imgproxy server.

    Attributes:
        value: Animation frame resolution limit in megapixels.

    Usage:

    >>> option = MaxAnimationFrameResolution(20)
    >>> option.arguments
    (20,)

    See `imgproxy max animation frame resolution
    <https://docs.imgproxy.net/usage/processing#max-animation-frame-resolution>`_.
    """

    name: ClassVar[str] = 'max_animation_frame_resolution'
    short_name: ClassVar[str | None] = 'mafr'
