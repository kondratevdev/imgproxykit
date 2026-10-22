from typing import Literal

type Argument = str | int | float | bool | None
"""
Scalar value accepted in an option's positional arguments.

Values in :attr:`~imgproxykit.options.Option.arguments`. Booleans become
``1`` or ``0``. ``None`` leaves an empty argument position; trailing
``None`` values are omitted by the default serializer.

See `imgproxy processing options
<https://docs.imgproxy.net/usage/processing#processing-options>`_.
"""

type FormatType = Literal[
    'png',
    'jpg',
    'jxl',
    'webp',
    'avif',
    'gif',
    'ico',
    'svg',
    'heic',
    'bmp',
    'tiff',
]
"""
Image format identifiers accepted by imgproxykit.

Formats for :class:`~imgproxykit.options.Format`,
:class:`~imgproxykit.options.FormatQuality`, and the ``format`` keyword
of :class:`~imgproxykit.Transform`. For example, use ``jpg`` for JPEG
and ``jxl`` for JPEG XL.

An identifier in this type does not guarantee output support on your
server. Supported input and output formats depend on the imgproxy build;
SVG output has additional restrictions.

See `imgproxy format
<https://docs.imgproxy.net/usage/processing#format>`_ and the
`image formats support matrix
<https://docs.imgproxy.net/image_formats_support>`_.
"""

type OptionType = Literal[
    'format',
    'preset',
    'width',
    'height',
    'min-width',
    'min-height',
    'resizing_type',
    'enlarge',
    'auto_rotate',
    'rotate',
    'blur',
    'sharpen',
    'pixelate',
    'strip_metadata',
    'keep_copyright',
    'strip_color_profile',
    'preserve_hdr',
    'enforce_thumbnail',
    'max_bytes',
    'raw',
    'expires',
    'return_attachment',
    'max_src_resolution',
    'max_src_file_size',
    'max_animation_frames',
    'max_animation_frame_resolution',
    'max_result_dimension',
    'size',
    'zoom',
    'extend',
    'extend_aspect_ratio',
    'crop',
    'trim',
    'padding',
    'flip',
    'background',
    'format_quality',
    'skip_processing',
    'filename',
    'cachebuster',
    'resize',
    'gravity',
    'dpr',
    'quality',
    'watermark',
]
"""
Processing option names represented by imgproxykit's built-in options.

Names in :attr:`~imgproxykit.options.Option.name` identify URL segments.
These are protocol names; scalar keywords in
:class:`~imgproxykit.Transform` replace hyphens with underscores.
For example, ``min-width`` corresponds to ``min_width``.

This type describes the library's supported names, rather than every
option available in every imgproxy version or edition.

See `imgproxy processing options
<https://docs.imgproxy.net/usage/processing#processing-options>`_.
"""

type WatermarkPosition = Literal[
    'ce',
    'no',
    'so',
    'ea',
    'we',
    'noea',
    'nowe',
    'soea',
    'sowe',
    're',
]
"""
Placement codes for :class:`~imgproxykit.options.Watermark`.

See `imgproxy watermark
<https://docs.imgproxy.net/usage/processing#watermark>`_.
"""

type ResizeType = Literal[
    'fit',
    'fill',
    'fill-down',
    'force',
    'auto',
]
"""
Resizing modes for :class:`~imgproxykit.options.Resize` and
:class:`~imgproxykit.options.ResizingType`.

See `imgproxy resizing type
<https://docs.imgproxy.net/usage/processing#resizing-type>`_.
"""

type Position = Literal[
    'no',
    'so',
    'ea',
    'we',
    'noea',
    'nowe',
    'soea',
    'sowe',
    'ce',
    'sm',
    'fp',
]
"""
Gravity codes for :class:`~imgproxykit.options.Gravity` and
:class:`~imgproxykit.options.Crop`.

See `imgproxy gravity
<https://docs.imgproxy.net/usage/processing#gravity>`_.
"""
