from imgproxykit.internal.paths import build_path
from imgproxykit.internal.serialization import serialize_option
from imgproxykit.transform import Transform
from imgproxykit.types import EMPTY, FormatType


class PathBuilder:
    """
    Resolve processing options and build an unsigned imgproxy path.

    Used by :class:`~imgproxykit.Client` before signing the resulting path.
    Sources are Base64-encoded without padding; processing options and an
    optional output extension are included in the same path.

    Transforms can combine processing options and server preset references.

    Subclass this builder and override :meth:`__call__` to customize path
    construction. Set the subclass on
    :attr:`imgproxykit.Client.path_builder_cls` to use it in a client.

    """

    __slots__ = ()

    # TODO: Support source_url_encryption_key for source URL encryption (Pro).
    # TODO: Support the plain option for unencoded source URLs.
    def __call__(
        self,
        source: str,
        *,
        transform: Transform | EMPTY = EMPTY,
    ) -> str:
        """
        Build a path from a transform containing processing options.

        Args:
            source: Complete source URI understood by imgproxy. Its contents
                are encoded as supplied, without resolving relative paths.
            transform: Processing options and optional output format.
                Omit to add no processing options.

        Returns:
            Unsigned path beginning with ``/``, ready for signing.
            Contains neither the imgproxy address nor a signature segment.

        Usage:

        >>> from imgproxykit import Transform
        >>> from imgproxykit.builders import PathBuilder
        >>> from imgproxykit.options import Preset, Resize
        >>> builder = PathBuilder()
        >>> source = 'https://example.com/photo.jpg'
        >>> thumbnail = Transform(
        ...     Resize(width=96, height=96, mode='fill'),
        ...     format='webp',
        ... )
        >>> local_path = builder(source, transform=thumbnail)
        >>> preset_path = builder(
        ...     source,
        ...     transform=Transform(
        ...         Preset(names=('thumbnail',)),
        ...         format='webp',
        ...     ),
        ... )

        """
        options, selected_format = self._resolve_options(
            transform,
        )
        return build_path(
            source,
            options=options,
            output_format=selected_format,
        )

    def _resolve_options(
        self,
        transform: Transform | EMPTY,
    ) -> tuple[tuple[str, ...], FormatType | EMPTY]:
        """
        Serialize options in supplied order and resolve the output format.

        Preset references remain in place alongside other processing options.

        """
        if transform is EMPTY:
            return (), EMPTY

        return (
            tuple(serialize_option(option) for option in transform.options),
            transform.format,
        )
