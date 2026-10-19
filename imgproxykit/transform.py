from imgproxykit.options import Option


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
    __slots__ = ('options',)

    def __init__(self, *options: Option) -> None:
        """Collect processing options in order."""
        self.options = options
