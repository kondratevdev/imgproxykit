from typing import Annotated, Any, ClassVar, get_args, get_type_hints

from typing_extensions import TypedDict

from imgproxykit import options
from imgproxykit.types import Argument, FormatType, ResizeType

type _ScalarOptionClass = type[options.ScalarOption[Any]]


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

    auto_rotate: Annotated[bool, options.AutoRotate]
    blur: Annotated[float, options.Blur]
    cache_buster: Annotated[str, options.CacheBuster]
    dpr: Annotated[float, options.DPR]
    enforce_thumbnail: Annotated[bool, options.EnforceThumbnail]
    enlarge: Annotated[bool, options.Enlarge]
    expires: Annotated[int, options.Expires]
    filename: Annotated[str, options.Filename]
    format: Annotated[FormatType, options.Format]
    height: Annotated[int, options.Height]
    keep_copyright: Annotated[bool, options.KeepCopyright]
    max_animation_frame_resolution: Annotated[
        float,
        options.MaxAnimationFrameResolution,
    ]
    max_animation_frames: Annotated[int, options.MaxAnimationFrames]
    max_bytes: Annotated[int, options.MaxBytes]
    max_result_dimension: Annotated[int, options.MaxResultDimension]
    max_src_file_size: Annotated[int, options.MaxSrcFileSize]
    max_src_resolution: Annotated[float, options.MaxSrcResolution]
    min_height: Annotated[int, options.MinHeight]
    min_width: Annotated[int, options.MinWidth]
    pixelate: Annotated[int, options.Pixelate]
    preserve_hdr: Annotated[bool, options.PreserveHDR]
    quality: Annotated[int, options.Quality]
    raw: Annotated[bool, options.Raw]
    resizing_type: Annotated[ResizeType, options.ResizingType]
    return_attachment: Annotated[bool, options.ReturnAttachment]
    rotate: Annotated[int, options.Rotate]
    sharpen: Annotated[float, options.Sharpen]
    strip_color_profile: Annotated[bool, options.StripColorProfile]
    strip_metadata: Annotated[bool, options.StripMetadata]
    width: Annotated[int, options.Width]


class KeywordOptionResolver:
    """Resolve built-in scalar options from Transform keywords."""

    __slots__ = ()

    _classes: ClassVar[dict[str, _ScalarOptionClass]] = _resolve_classes()

    @classmethod
    def from_kwarg(
        cls,
        keyword: str,
        value: Argument,
    ) -> options.ScalarOption[Any]:
        """Construct a built-in option from a Transform keyword."""
        option_cls = cls._classes.get(keyword)
        if option_cls is None:
            raise TypeError(
                f'Unknown scalar processing option {keyword!r}. '
                'Pass custom options as positional arguments.',
            )
        return option_cls(value)
