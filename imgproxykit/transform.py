from dataclasses import dataclass
from itertools import starmap
from typing import Unpack

from typing_extensions import TypedDict

from imgproxykit.options import Option, ScalarOption
from imgproxykit.types import FormatType, ResizeType


class ScalarOptions(TypedDict, total=False, closed=True):
    """Optional scalar processing arguments accepted by Transform."""

    auto_rotate: bool
    blur: float
    cachebuster: str
    dpr: float
    enforce_thumbnail: bool
    enlarge: bool
    expires: int
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


@dataclass(frozen=True, slots=True)
class Transform:
    """
    Define reusable image processing options.

    Options are serialized in the supplied order. Imgproxy determines the
    image processing pipeline and resolves omitted option arguments using
    its defaults.

    Attributes:
        options: Tuple of processing options. Defaults to an empty tuple,
            which adds no processing option segments to the URL.

    Usage:

    >>> from imgproxykit import Client, Transform
    >>> from imgproxykit.options import Format, Quality, Resize
    >>> thumbnail = Transform(
    ...     Resize(width=300, height=300, mode='fill'),
    ...     Quality(85),
    ...     Format('webp'),
    ... )
    >>> client = Client('https://images.example.com')
    >>> url = client.url(
    ...     'https://example.com/image.jpg',
    ...     transform=thumbnail,
    ... )

    """

    # TODO: Add immutable derivation with explicit append/replace/remove
    # semantics. Define conflicts between overlapping options (Resize, Size,
    # Width, Height), repeated options, and server presets without expanding
    # preset definitions locally. Support clearing inherited options to
    # restore server defaults.
    # TODO: Document with examples that option order controls serialization
    # and overrides, while imgproxy determines the processing pipeline.
    options: tuple[Option, ...]

    def __init__(
        self,
        *options: Option,
        **kwargs: Unpack[ScalarOptions],
    ) -> None:
        """Collect positional options, followed by scalar keyword options."""
        # Keep variadic options while initializing a frozen dataclass.
        # Bypassing __setattr__ is safe until initialization is finished.
        scalar_options = tuple(starmap(ScalarOption.from_kwarg, kwargs.items()))
        object.__setattr__(self, 'options', (*options, *scalar_options))
