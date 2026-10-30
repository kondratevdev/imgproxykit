from collections.abc import Callable

from imgproxykit.internal.encoding import encode_base64, encode_plain
from imgproxykit.transform import Transform
from imgproxykit.types import Argument, SourceEncoding


class PathSerializer:
    """
    Serialize processing options into an unsigned imgproxy path.

    Used by :class:`~imgproxykit.Client` before signing the resulting path.
    Sources use URL-safe Base64 without padding or full percent-encoding.
    Processing options precede the source in the supplied order.

    Pass processing options through :class:`~imgproxykit.Transform` as
    option instances or scalar keyword arguments. Preset options reference
    names configured on the imgproxy server and are not expanded here.

    Subclass this serializer and override :meth:`__call__` to customize path
    construction. Set the subclass on
    :attr:`imgproxykit.Client.path_serializer_cls` to use it in a client.

    """

    __slots__ = (
        '_argument_separator',
        '_source_serializer',
        '_use_short_options',
    )

    def __init__(
        self,
        *,
        argument_separator: str,
        use_short_options: bool,
        source_encoding: SourceEncoding,
    ) -> None:
        """
        Configure processing options and select the source URL serializer.

        Args:
            argument_separator: Separator between processing option names
                and their arguments. Must match the server's
                `IMGPROXY_ARGUMENTS_SEPARATOR
                <https://docs.imgproxy.net/latest/configuration/options#miscellaneous>`__.
            use_short_options: Use short aliases when available,
                otherwise full names.
            source_encoding: Source URL representation: ``'base64'`` without
                padding or ``'plain'`` with full UTF-8 percent-encoding.
                See `imgproxy source URLs
                <https://docs.imgproxy.net/usage/processing#source-url>`_.

        """
        self._argument_separator = argument_separator
        self._use_short_options = use_short_options
        self._source_serializer = self._resolve_source_serializer(
            source_encoding,
        )

    def __call__(
        self,
        source: str,
        *,
        transform: Transform | None = None,
    ) -> str:
        """
        Build an unsigned path using processing options and preset references.

        Serialize each option using the configured arguments separator before
        the encoded source. Output formats are included as processing segments.
        Omitted processing parameters are left to the server.

        Args:
            source: Complete source URI understood by the imgproxy server.
                Encoded according to ``source_encoding``.
            transform: Reusable processing options and optional output format.
                Omit or pass ``None`` to add no processing options.

        Returns:
            Unsigned path beginning with ``/``, ready for signing.
            Contains neither the imgproxy address nor a signature segment.

        Examples:
            Build a square WebP thumbnail path:

            >>> from imgproxykit import Transform
            >>> from imgproxykit.serialization import PathSerializer
            >>> from imgproxykit.options import Resize
            >>> serializer = PathSerializer(
            ...     argument_separator=':',
            ...     use_short_options=False,
            ...     source_encoding='base64',
            ... )
            >>> thumbnail = Transform(
            ...     Resize.fill(width=96, height=96),
            ...     format='webp',
            ... )
            >>> serializer('s3://images/photo.jpg', transform=thumbnail)
            '/resize:fill:96:96/format:webp/czM6Ly9pbWFnZXMvcGhvdG8uanBn'

        """
        options: tuple[str, ...] = ()
        if transform is not None:
            options = tuple(
                self._serialize_segment(
                    (option.short_name or option.name)
                    if self._use_short_options
                    else option.name,
                    option.arguments,
                )
                for option in transform.options
            )
        return '/'.join(('', *options, self._source_serializer(source)))

    def _resolve_source_serializer(
        self,
        source_encoding: SourceEncoding,
    ) -> Callable[[str], str]:
        """
        Select source path serialization once during initialization.

        The callable returns the encoded source with any required path marker,
        ready to append after processing options and include in the signature.
        """
        return (
            encode_base64
            if source_encoding == 'base64'
            else self._serialize_plain_source
        )

    @classmethod
    def _serialize_plain_source(cls, source: str) -> str:
        """
        Prefix the percent-encoded source with imgproxy's plain path marker.

        Encode only the source so that the separating slash remains part of
        the imgproxy path. Output formats remain processing option segments.

        The ``/plain/`` segment identifies a percent-encoded source URL.
        See `imgproxy plain source URLs
        <https://docs.imgproxy.net/usage/processing#plain>`_.
        """
        return f'plain/{encode_plain(source)}'

    def _serialize_segment(
        self,
        name: str,
        arguments: tuple[Argument, ...],
    ) -> str:
        """
        Serialize an option name and positional arguments into a path segment.

        Internal ``None`` values become empty positions; trailing ``None``
        values are omitted. Explicit zeroes and empty strings retain their
        positions. Booleans are serialized as ``1`` and ``0``.

        """
        # TODO: Verify reserved characters in string arguments and preset names
        # against imgproxy before choosing encoding or rejection.
        end = len(arguments)
        while end and arguments[end - 1] is None:
            end -= 1

        serialized = map(self._serialize_argument, arguments[:end])
        return self._argument_separator.join((name, *serialized))

    @classmethod
    def _serialize_argument(cls, value: Argument) -> str:
        """Serialize one argument without treating false values as omitted."""
        if value is None:
            return ''
        if isinstance(value, bool):
            return str(int(value))
        return str(value)
