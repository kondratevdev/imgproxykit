from typing import ClassVar, overload

from imgproxykit.builders import PathBuilder
from imgproxykit.signing import URLSigner
from imgproxykit.transform import Transform
from imgproxykit.types import EMPTY, FormatType


class Client:
    """
    Build imgproxy URLs from Python transforms or server presets.

    Stores the imgproxy address and signing configuration for reuse across
    images. Each call to :meth:`url` returns a URL string; imgproxy loads
    the source and processes the image when that URL is requested.

    Processing parameters can come from a :class:`~imgproxykit.Transform`
    defined in Python or from preset names configured on the imgproxy server.

    Subclass this client and override :attr:`path_builder_cls` or
    :attr:`signer_cls` to customize path construction or signing.
    Each client creates its own instances of these components.

    """

    __slots__ = (
        '_base_url',
        '_path_builder',
        '_signer',
    )

    #: Component that resolves processing parameters and builds unsigned paths.
    path_builder_cls: ClassVar[type[PathBuilder]] = PathBuilder
    #: Component that signs paths or returns the unsigned URL marker.
    signer_cls: ClassVar[type[URLSigner]] = URLSigner

    @overload
    def __init__(
        self,
        base_url: str,
        /,
        *,
        unsigned_signature: str = 'unsafe',
    ) -> None: ...

    @overload
    def __init__(
        self,
        base_url: str,
        /,
        *,
        key: str,
        salt: str,
        signature_size: int = 32,
    ) -> None: ...

    def __init__(
        self,
        base_url: str,
        /,
        *,
        key: str | EMPTY = EMPTY,
        salt: str | EMPTY = EMPTY,
        signature_size: int = 32,
        unsigned_signature: str = 'unsafe',
    ) -> None:
        """
        Configure the imgproxy address and create the client components.

        Supply both ``key`` and ``salt`` for signed URLs. Omit both for
        URLs with an ``unsafe`` signature marker, which can be used with
        an imgproxy server that has signature checking disabled.

        Args:
            base_url: Public imgproxy address, including any deployment path
                prefix. Required positional argument. Trailing slashes
                are removed.
            unsigned_signature: URL marker used when key and salt are omitted.
                Defaults to 'unsafe'. With server signing enabled, configure
                this marker in IMGPROXY_TRUSTED_SIGNATURES.
            key: Hex-encoded signing key matching the server configuration.
            salt: Hex-encoded signing salt matching the server configuration.
            signature_size: Positive digest byte count to encode. Must match
                the server's IMGPROXY_SIGNATURE_SIZE. Defaults to 32.
                Values of 32 or more use the full digest.

        Raises:
            ValueError: With the default signer, if only one signing
                credential is supplied, either is empty or invalid hex,
                or signature_size is not positive.

        Usage:

        >>> from imgproxykit import Client
        >>> unsigned = Client('https://images.example.com')
        >>> signed = Client(
        ...     'https://images.example.com',
        ...     key='736563726574',
        ...     salt='73616c74',
        ... )

        The signing credentials above are examples for local development.

        """
        # TODO: Define runtime validation for base URLs and empty sources.
        self._base_url = base_url.rstrip('/')
        self._path_builder = self.path_builder_cls()
        self._signer = self.signer_cls(
            key=key,
            salt=salt,
            signature_size=signature_size,
            unsigned_signature=unsigned_signature,
        )

    # TODO: Remove the separate format argument once Format is an option;
    # express format-only URLs and presets with formats through Transform.
    @overload
    def url(
        self,
        source: str,
        *,
        transform: Transform | EMPTY = ...,
    ) -> str: ...

    @overload
    def url(
        self,
        source: str,
        *,
        presets: tuple[str, ...],
        format: FormatType | EMPTY = EMPTY,
    ) -> str: ...

    def url(
        self,
        source: str,
        *,
        transform: Transform | EMPTY = EMPTY,
        presets: tuple[str, ...] | EMPTY = EMPTY,
        format: FormatType | EMPTY = EMPTY,  # noqa: A002
    ) -> str:
        """
        Build a URL for one source using a transform or server presets.

        Pass ``transform`` for processing parameters defined in Python.
        Pass ``presets`` to reference named server presets instead.
        Preset definitions remain on the server and are not expanded here.

        With a Python transform, set the output format on that transform.
        With server presets, use the ``format`` argument. Omitted processing
        parameters and formats are left to the server.

        Args:
            source: Complete source URI understood by the imgproxy server.
                The default builder Base64-encodes it without changing its
                contents or resolving storage-relative paths.
            transform: Reusable processing options and optional output format.
                Omitting both ``transform`` and ``presets`` adds no options.
            presets: Names of server presets, in the supplied order.
                Mutually exclusive with ``transform``.
            format: Output format when using ``presets``. Must be omitted
                when using a Python transform.

        Returns:
            The complete imgproxy URL, signed when credentials were supplied.

        Raises:
            ValueError: With the default builder, if ``transform`` and
                ``presets`` are supplied together, or ``format`` is supplied
                without ``presets``.

        Usage:

        >>> from imgproxykit import Client, Transform
        >>> from imgproxykit.options import Resize
        >>> client = Client('https://images.example.com')
        >>> thumbnail = Transform(
        ...     options=(Resize(width=300, height=300, mode='fill'),),
        ...     format='webp',
        ... )
        >>> source = 'https://example.com/photo.jpg'
        >>> local_options_url = client.url(source, transform=thumbnail)
        >>> server_presets_url = client.url(
        ...     source,
        ...     presets=('thumbnail', 'watermarked'),
        ...     format='webp',
        ... )

        """
        path = self._path_builder(
            source,
            transform=transform,
            presets=presets,
            output_format=format,
        )
        signature = self._signer(path)
        return f'{self._base_url}/{signature}{path}'
