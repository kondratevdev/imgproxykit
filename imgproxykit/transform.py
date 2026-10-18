from imgproxykit.options import Option
from imgproxykit.types import EMPTY, FormatType


class Transform:
    """
    Define reusable image processing options.

    Options are serialized in the supplied order. Imgproxy determines the
    image processing pipeline and resolves omitted option arguments using
    its defaults.

    Attributes:
        options: Tuple of processing options. Defaults to an empty tuple,
            which adds no processing option segments to the URL.
        format: Output image format, such as ``webp`` or ``avif``.
            Defaults to :data:`~imgproxykit.types.EMPTY`, leaving format
            selection to imgproxy.

    Usage:

    >>> from imgproxykit import Client, Transform
    >>> from imgproxykit.options import Quality, Resize
    >>> thumbnail = Transform(
    ...     Resize(width=300, height=300, mode='fill'),
    ...     Quality(85),
    ...     format='webp',
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
    # preset definitions locally. Support format overrides and clearing
    # inherited options or format to restore server defaults.
    # TODO: Document with examples that option order controls serialization
    # and overrides, while imgproxy determines the processing pipeline.
    __slots__ = ('format', 'options')

    # TODO: Move format into a typed Format option alongside other components
    # and serialize it as an f segment. Remove this separate field and use
    # the common option composition and replacement rules for formats.
    def __init__(
        self,
        *options: Option,
        format: FormatType | EMPTY = EMPTY,  # noqa: A002
    ) -> None:
        """Collect processing options in order and set the output format."""
        self.options = options
        self.format = format
