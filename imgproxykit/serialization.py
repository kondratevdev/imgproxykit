from imgproxykit.internal.encoding import encode_base64
from imgproxykit.transform import Transform
from imgproxykit.types import Argument


class PathSerializer:
    """
    Serialize processing options into an unsigned imgproxy path.

    Used by :class:`~imgproxykit.Client` before signing the resulting path.
    Sources are encoded as URL-safe Base64 without padding. Processing
    options are included before the source in the supplied order.

    Pass processing options through :class:`~imgproxykit.Transform` as
    option instances or scalar keyword arguments. Preset options reference
    names configured on the imgproxy server and are not expanded here.

    Subclass this serializer and override :meth:`__call__` to customize path
    construction. Set the subclass on
    :attr:`imgproxykit.Client.path_serializer_cls` to use it in a client.

    """

    __slots__ = ('_arguments_separator',)

    # TODO: Support the plain option for unencoded source URLs.
    def __init__(self, *, arguments_separator: str) -> None:
        """
        Configure processing option serialization.

        Args:
            arguments_separator: Separator between processing option names
                and their arguments. Must match the server's
                `IMGPROXY_ARGUMENTS_SEPARATOR
                <https://docs.imgproxy.net/latest/configuration/options#miscellaneous>`__.

        """
        self._arguments_separator = arguments_separator

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
                Its UTF-8 representation is encoded as URL-safe Base64
                without padding. The URI is neither validated nor resolved.
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
            >>> serializer = PathSerializer(arguments_separator=':')
            >>> thumbnail = Transform(
            ...     Resize(width=96, height=96, mode='fill'),
            ...     format='webp',
            ... )
            >>> serializer('s3://images/photo.jpg', transform=thumbnail)
            '/resize:fill:96:96/format:webp/czM6Ly9pbWFnZXMvcGhvdG8uanBn'

        """
        options = (
            ()
            if transform is None
            else tuple(
                self._serialize_segment(option.name, option.arguments)
                for option in transform.options
            )
        )
        return '/'.join(('', *options, encode_base64(source)))

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
        return self._arguments_separator.join((name, *serialized))

    @classmethod
    def _serialize_argument(cls, value: Argument) -> str:
        """Serialize one argument without treating false values as omitted."""
        if value is None:
            return ''
        if isinstance(value, bool):
            return str(int(value))
        return str(value)
