from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import ResizingAlgorithmType


@dataclass(frozen=True, slots=True)
class ResizingAlgorithm(ScalarOption[ResizingAlgorithmType]):
    """
    Choose the algorithm used for resizing (imgproxy Pro).

    Imgproxy defaults to ``lanczos3`` when this option is omitted.

    Attributes:
        value: Resizing algorithm: ``nearest``, ``linear``, ``cubic``,
            ``lanczos2``, or ``lanczos3``.

    Usage:

    >>> option = ResizingAlgorithm('lanczos3')
    >>> option.arguments
    ('lanczos3',)

    See `imgproxy resizing algorithm
    <https://docs.imgproxy.net/usage/processing#resizing-algorithm>`_.
    """

    name: ClassVar[str] = 'resizing_algorithm'
    short_name: ClassVar[str | None] = 'ra'
