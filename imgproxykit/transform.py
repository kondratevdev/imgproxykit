from dataclasses import dataclass
from datetime import datetime, timedelta
from itertools import starmap
from typing import Unpack

from typing_extensions import TypedDict

from imgproxykit.options import Option, ScalarOption
from imgproxykit.types import FormatType, ResizeType


class ScalarOptions(TypedDict, total=False, closed=True):
    """Optional scalar processing arguments accepted by :class:`Transform`."""

    auto_rotate: bool
    blur: float
    cachebuster: str
    dpr: float
    enforce_thumbnail: bool
    enlarge: bool
    expires: int | datetime | timedelta
    filename: str
    format: FormatType
    height: int
    keep_copyright: bool
    max_animation_frame_resolution: float
    max_animation_frames: int
    max_bytes: int
    max_result_dimension: int
    max_src_file_size: int
    max_src_resolution: float
    min_height: int
    min_width: int
    pixelate: int
    preserve_hdr: bool
    quality: int
    raw: bool
    resizing_type: ResizeType
    return_attachment: bool
    rotate: int
    sharpen: float
    strip_color_profile: bool
    strip_metadata: bool
    width: int


@dataclass(frozen=True, slots=True, init=False)
class Transform:
    """
    Define reusable image processing options.

    Stores an immutable tuple of options for reuse with
    :meth:`imgproxykit.Client.url`. Pass option instances or scalar keyword
    arguments; scalar options follow the positional options in keyword order.

    Options retain their supplied order during serialization. Imgproxy
    determines the image processing pipeline and resolves omitted arguments
    using its defaults. Preset options reference names configured on the
    imgproxy server and are not expanded here.

    Attributes:
        options: Tuple of processing options. Defaults to an empty tuple,
            which adds no processing option segments to the URL.

    """

    options: tuple[Option, ...]

    def __init__(
        self,
        *options: Option,
        **kwargs: Unpack[ScalarOptions],
    ) -> None:
        """
        Collect positional options, followed by scalar keyword options.

        Args:
            *options: Processing option instances in serialization order.
                Repeated options are retained without merging.
            **kwargs: Scalar processing arguments, such as ``quality=85``
                or ``format='webp'``. Converted to option instances and
                appended in keyword order.

        Examples:
            Combine a resize option with scalar quality and format options:

            >>> from imgproxykit import Transform
            >>> from imgproxykit.options import Resize
            >>> thumbnail = Transform(
            ...     Resize(width=96, height=96, mode='fill'),
            ...     quality=85,
            ...     format='webp',
            ... )
            >>> [option.name for option in thumbnail.options]
            ['resize', 'quality', 'format']

        """
        # Keep variadic options while initializing a frozen dataclass.
        # Bypassing __setattr__ is safe until initialization is finished.
        scalar_options = tuple(starmap(ScalarOption.from_kwarg, kwargs.items()))
        object.__setattr__(self, 'options', (*options, *scalar_options))
