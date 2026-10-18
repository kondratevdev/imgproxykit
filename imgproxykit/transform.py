from dataclasses import dataclass

from imgproxykit.options import Option
from imgproxykit.types import EMPTY, FormatType


@dataclass(frozen=True, slots=True, kw_only=True)
class Transform:
    """
    Define reusable image processing options and an optional output format.

    Instances are immutable and can be reused for multiple source images
    and clients. Pass a transform to :meth:`imgproxykit.Client.url` to
    include its processing options and output format in the generated URL.

    Options are serialized in the supplied order. imgproxy determines the
    image processing pipeline and resolves omitted option arguments using
    its defaults. Creating a transform does not process an image or make
    a network request.

    Attributes:
        options: Tuple of typed processing options. Defaults to an empty
            tuple, which adds no processing option segments to the URL.
        format: Output image format, such as ``webp`` or ``avif``.
            Defaults to :data:`~imgproxykit.types.EMPTY`, leaving format
            selection to imgproxy.

    Usage:

    >>> from imgproxykit import Client, Transform
    >>> from imgproxykit.options import Quality, Resize
    >>> thumbnail = Transform(
    ...     options=(
    ...         Resize(width=300, height=300, mode='fill'),
    ...         Quality(85),
    ...     ),
    ...     format='webp',
    ... )
    >>> client = Client('https://images.example.com')
    >>> first_url = client.url(
    ...     'https://example.com/first.jpg',
    ...     transform=thumbnail,
    ... )
    >>> second_url = client.url(
    ...     'https://example.com/second.jpg',
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
    # TODO: Accept positional *options instead of options=(...), preserving
    # immutable tuple storage; update examples and public API typing tests.
    options: tuple[Option, ...] = ()
    # TODO: Move format into a typed Format option alongside other components
    # and serialize it as an f segment. Remove this separate field and use
    # the common option composition and replacement rules for formats.
    format: FormatType | EMPTY = EMPTY
