from imgproxykit.internal.constants import PRESET
from imgproxykit.internal.paths import build_path
from imgproxykit.internal.serialization import (
    serialize_option,
    serialize_segment,
)
from imgproxykit.transform import Transform
from imgproxykit.types import EMPTY, FormatType


class PathBuilder:
    """
    Resolve processing options and build an unsigned imgproxy path.

    Used by :class:`~imgproxykit.Client` before signing the resulting path.
    Sources are Base64-encoded without padding; processing options and an
    optional output extension are included in the same path.

    Python transforms and server presets are mutually exclusive.
    Preset definitions remain on the imgproxy server.

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
        presets: tuple[str, ...] | EMPTY = EMPTY,
        output_format: FormatType | EMPTY = EMPTY,
    ) -> str:
        """
        Build a path from a Python transform or server preset names.

        Args:
            source: Complete source URI understood by imgproxy. Its contents
                are encoded as supplied, without resolving relative paths.
            transform: Processing options and output format defined in Python.
                Omit together with ``presets`` to add no processing options.
            presets: Server preset names in the order they should be supplied.
                Cannot be combined with ``transform``.
            output_format: Output extension when using ``presets``.
                For a Python transform, set its ``format`` instead.

        Returns:
            Unsigned path beginning with ``/``, ready for signing.
            Contains neither the imgproxy address nor a signature segment.

        Raises:
            ValueError: If ``transform`` and ``presets`` are both supplied,
                or ``output_format`` is supplied without ``presets``.

        Usage:

        >>> from imgproxykit import Transform
        >>> from imgproxykit.builders import PathBuilder
        >>> from imgproxykit.options import Resize
        >>> builder = PathBuilder()
        >>> source = 'https://example.com/photo.jpg'
        >>> thumbnail = Transform(
        ...     options=(Resize(width=96, height=96, mode='fill'),),
        ...     format='webp',
        ... )
        >>> local_path = builder(source, transform=thumbnail)
        >>> preset_path = builder(
        ...     source,
        ...     presets=('thumbnail',),
        ...     output_format='webp',
        ... )

        """
        options, selected_format = self._resolve_options(
            transform,
            presets,
            output_format,
        )
        return build_path(
            source,
            options=options,
            output_format=selected_format,
        )

    def _resolve_options(
        self,
        transform: Transform | EMPTY,
        presets: tuple[str, ...] | EMPTY,
        output_format: FormatType | EMPTY,
    ) -> tuple[tuple[str, ...], FormatType | EMPTY]:
        """
        Resolve mutually exclusive inputs into path segments and a format.

        Python options are serialized in their supplied order. Server preset
        names form a single ``pr`` segment. Omitted processing parameters
        produce no segments and leave the output format unspecified.

        """
        self._validate_options(transform, presets, output_format)
        if presets is not EMPTY:
            return (serialize_segment(PRESET, presets),), output_format

        if transform is EMPTY:
            return (), EMPTY

        return (
            tuple(serialize_option(option) for option in transform.options),
            transform.format,
        )

    def _validate_options(
        self,
        transform: Transform | EMPTY,
        presets: tuple[str, ...] | EMPTY,
        output_format: FormatType | EMPTY,
    ) -> None:
        """
        Validate processing options before path serialization.

        Python transforms cannot be combined with server presets.
        A separate output format is only accepted with server presets.

        """
        # TODO: Support server presets together with Python options; imgproxy
        # allows both in one URL. Consider a typed Preset option in Transform
        # and define ordering before relaxing this validation.
        if transform is not EMPTY and presets is not EMPTY:
            raise ValueError('Choose transform or presets.')

        if presets is EMPTY and output_format is not EMPTY:
            raise ValueError('Set format on the Python transform.')
