from dataclasses import dataclass
from itertools import starmap
from typing import (
    Annotated,
    Any,
    ClassVar,
    Unpack,
    get_args,
    get_type_hints,
)

from typing_extensions import TypedDict

from imgproxykit import options as opts
from imgproxykit.types import Argument, FormatType, ResizeType

type _ScalarOptionClass = type[opts.ScalarOption[Any]]


def _resolve_classes() -> dict[str, _ScalarOptionClass]:
    hints = get_type_hints(KeywordOptions, include_extras=True)
    classes = {}
    for keyword, annotation in hints.items():
        _, option_cls = get_args(annotation)
        classes[keyword] = option_cls
    return classes  # pyright: ignore[reportUnknownVariableType]


class KeywordOptions(TypedDict, total=False, closed=True):
    """
    Built-in scalar keyword arguments for :class:`~imgproxykit.Transform`.

    All keywords are optional and are also accepted by
    :meth:`~imgproxykit.Transform.extend`. Each field declares the value type
    and carries the corresponding option class in its ``Annotated`` metadata.

    The field name is the Python keyword. The option class defines the name
    used in the URL. For example, ``cache_buster="v2"`` creates a
    ``CacheBuster`` option with the URL segment ``cachebuster:v2`` when using
    the default separator and full option names.

    Pass custom processing options as positional
    :class:`~imgproxykit.options.Option` instances.
    """

    auto_rotate: Annotated[bool, opts.AutoRotate]
    blur: Annotated[float, opts.Blur]
    cache_buster: Annotated[str, opts.CacheBuster]
    dpr: Annotated[float, opts.DPR]
    enforce_thumbnail: Annotated[bool, opts.EnforceThumbnail]
    enlarge: Annotated[bool, opts.Enlarge]
    expires: Annotated[int, opts.Expires]
    filename: Annotated[str, opts.Filename]
    format: Annotated[FormatType, opts.Format]
    height: Annotated[int, opts.Height]
    keep_copyright: Annotated[bool, opts.KeepCopyright]
    max_animation_frame_resolution: Annotated[
        float,
        opts.MaxAnimationFrameResolution,
    ]
    max_animation_frames: Annotated[int, opts.MaxAnimationFrames]
    max_bytes: Annotated[int, opts.MaxBytes]
    max_result_dimension: Annotated[int, opts.MaxResultDimension]
    max_src_file_size: Annotated[int, opts.MaxSrcFileSize]
    max_src_resolution: Annotated[float, opts.MaxSrcResolution]
    min_height: Annotated[int, opts.MinHeight]
    min_width: Annotated[int, opts.MinWidth]
    pixelate: Annotated[int, opts.Pixelate]
    preserve_hdr: Annotated[bool, opts.PreserveHDR]
    quality: Annotated[int, opts.Quality]
    raw: Annotated[bool, opts.Raw]
    resizing_type: Annotated[ResizeType, opts.ResizingType]
    return_attachment: Annotated[bool, opts.ReturnAttachment]
    rotate: Annotated[int, opts.Rotate]
    sharpen: Annotated[float, opts.Sharpen]
    strip_color_profile: Annotated[bool, opts.StripColorProfile]
    strip_metadata: Annotated[bool, opts.StripMetadata]
    width: Annotated[int, opts.Width]


class KeywordOptionResolver:
    """Resolve built-in scalar options from Transform keywords."""

    __slots__ = ()

    _classes: ClassVar[dict[str, _ScalarOptionClass]] = _resolve_classes()

    @classmethod
    def from_kwarg[KwargValueT: Argument](
        cls,
        keyword: str,
        value: KwargValueT,
    ) -> opts.ScalarOption[KwargValueT]:
        """Construct a built-in option from a Transform keyword."""
        option_cls = cls._classes.get(keyword)
        if option_cls is None:
            raise TypeError(
                f'Unknown scalar processing option {keyword!r}. '
                'Pass custom options as positional arguments.',
            )
        return option_cls(value)


@dataclass(frozen=True, slots=True, init=False)
class Transform:
    """
    Define reusable image processing options.

    Stores an immutable tuple of options for reuse with
    :meth:`imgproxykit.Client.url`. Pass option instances or scalar keyword
    arguments; scalar options follow the positional options in keyword order.
    Use :meth:`extend` to create a new transformation with additional options
    without changing the original.

    Options retain their supplied order during serialization. Imgproxy
    determines the image processing pipeline and resolves omitted arguments
    using its defaults. Preset options reference names configured on the
    imgproxy server and are not expanded here.

    Attributes:
        options: Tuple of processing options. Defaults to an empty tuple,
            which adds no processing option segments to the URL.
    """

    #: Component that resolves built-in scalar keyword options.
    keyword_option_resolver_cls: ClassVar[type[KeywordOptionResolver]] = (
        KeywordOptionResolver
    )

    options: tuple[opts.Option, ...]

    def __init__(
        self,
        *options: opts.Option,
        **kwargs: Unpack[KeywordOptions],
    ) -> None:
        """
        Collect positional options, followed by scalar keyword options.

        Args:
            *options: Processing option instances in serialization order.
                Repeated options are retained without merging.
            **kwargs: Scalar processing arguments, such as ``quality=85``
                or ``format='webp'``. Converted to option instances and
                appended in keyword order.
        """
        # Keep variadic options while initializing a frozen dataclass.
        # Bypassing __setattr__ is safe until initialization is finished.
        scalar_options = tuple(
            starmap(
                self.keyword_option_resolver_cls.from_kwarg,
                kwargs.items(),
            ),
        )
        object.__setattr__(self, 'options', (*options, *scalar_options))

    def extend(
        self,
        *options: opts.Option,
        **kwargs: Unpack[KeywordOptions],
    ) -> 'Transform':
        """
        Return a new transformation with additional processing options.

        The original transformation remains unchanged. Existing options are
        followed by positional options, then scalar keyword options in keyword
        order. Repeated options are retained without merging or replacing them.

        Args:
            *options: Processing option instances in serialization order.
                Repeated options are retained without merging.
            **kwargs: Scalar processing arguments, such as ``quality=85``
                or ``format='webp'``. Converted to option instances and
                appended in keyword order.
        """
        return type(self)(*self.options, *options, **kwargs)
