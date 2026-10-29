from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class MaxAnimationFrames(ScalarOption[int]):
    """
    Override animation frame limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    `IMGPROXY_ALLOW_SECURITY_OPTIONS
    <https://docs.imgproxy.net/latest/configuration/options#security>`__
    set to ``true`` on the imgproxy server.

    Attributes:
        value: Maximum number of animation frames.

    Usage:

    >>> option = MaxAnimationFrames(100)
    >>> option.arguments
    (100,)

    See `imgproxy max animation frames
    <https://docs.imgproxy.net/usage/processing#max-animation-frames>`_.

    """

    name: ClassVar[str] = 'max_animation_frames'
    short_name: ClassVar[str | None] = 'maf'
