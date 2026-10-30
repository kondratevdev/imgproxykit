from collections.abc import Mapping
from typing import ClassVar, overload

from imgproxykit.serialization import PathSerializer
from imgproxykit.signing import UrlSigner
from imgproxykit.transform import Transform


class Client:
    """
    Build imgproxy URLs from Python transforms or server presets.

    Stores the imgproxy address and signing configuration for reuse across
    images. Each call to :meth:`url` returns a URL string; imgproxy loads
    the source and processes the image when that URL is requested.

    Pass processing options through :class:`~imgproxykit.Transform` as
    option instances or scalar keyword arguments. Preset options reference
    names configured on the imgproxy server.

    Subclass this client and override :attr:`path_serializer_cls` or
    :attr:`url_signer_cls` to customize path construction or signing.
    Each client creates its own instances of these components.

    """

    __slots__ = (
        '_base_url',
        '_path_serializer',
        '_url_signer',
    )

    #: Component that resolves processing parameters and builds unsigned paths.
    path_serializer_cls: ClassVar[type[PathSerializer]] = PathSerializer
    #: Component that signs paths or returns the unsigned URL marker.
    url_signer_cls: ClassVar[type[UrlSigner]] = UrlSigner

    @overload
    def __init__(
        self,
        base_url: str,
        /,
        *,
        key: None = None,
        salt: None = None,
        unsigned_marker: str = 'unsafe',
        argument_separator: str = ':',
        use_short_options: bool = False,
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
        argument_separator: str = ':',
        use_short_options: bool = False,
    ) -> None: ...

    def __init__(  # noqa: WPS211
        self,
        base_url: str,
        /,
        *,
        key: str | None = None,
        salt: str | None = None,
        signature_size: int = 32,
        unsigned_marker: str = 'unsafe',
        argument_separator: str = ':',
        use_short_options: bool = False,
    ) -> None:
        """
        Configure the imgproxy address and create the client components.

        Supply both ``key`` and ``salt`` for signed URLs. Omit both for
        URLs with the configured unsigned marker (``unsafe`` by default).
        The server must accept unsigned requests or trust that marker.

        Args:
            base_url: Public imgproxy address, including any deployment path
                prefix. Trailing slashes are removed; the address is otherwise
                stored as supplied, without validation.
            key: Nonempty hex-encoded signing key matching the server.
                Supply together with ``salt``; ``None`` selects unsigned mode.
            salt: Nonempty hex-encoded signing salt matching the server.
                Supply together with ``key``; ``None`` selects unsigned mode.
            signature_size: Positive digest byte count to encode. Must match
                the server's `IMGPROXY_SIGNATURE_SIZE
                <https://docs.imgproxy.net/latest/configuration/options#url-signature>`__.
                Defaults to ``32``.
                Values of 32 or more use the full digest.
            unsigned_marker: URL marker used when key and salt are omitted.
                Defaults to ``'unsafe'``. With server signing enabled,
                configure this marker in `IMGPROXY_TRUSTED_SIGNATURES
                <https://docs.imgproxy.net/latest/configuration/options#url-signature>`__.
            argument_separator: Separator between processing option names
                and their arguments. Must match the server's
                `IMGPROXY_ARGUMENTS_SEPARATOR
                <https://docs.imgproxy.net/latest/configuration/options#miscellaneous>`__.
                Defaults to ``':'``.
            use_short_options: Use short processing option aliases when
                available, falling back to full names. Defaults to ``False``.

        Raises:
            ValueError: With the default signer, if only one signing
                credential is supplied, either is empty or invalid hex,
                or ``signature_size`` is not positive, even in unsigned mode.

        Examples:
            Create an unsigned client:

            >>> from imgproxykit import Client
            >>> client = Client('https://imgproxy.example.com')

            Create a signed client with example credentials:

            >>> client = Client(
            ...     'https://imgproxy.example.com',
            ...     key='736563726574',
            ...     salt='73616c74',
            ... )

        """
        # Prepare `base_url` only once pre instance
        self._base_url = base_url.rstrip('/')
        self._path_serializer = self.path_serializer_cls(
            argument_separator=argument_separator,
            use_short_options=use_short_options,
        )
        self._url_signer = self.url_signer_cls(
            key=key,
            salt=salt,
            signature_size=signature_size,
            unsigned_marker=unsigned_marker,
        )

    def url(
        self,
        source: str,
        *,
        transform: Transform | None = None,
    ) -> str:
        """
        Build a URL using processing options and server preset references.

        Pass option instances or scalar keyword arguments through
        :class:`~imgproxykit.Transform`. Use
        :class:`~imgproxykit.options.Preset` to reference server presets.
        Preset definitions remain on the server and are not expanded here.
        Set the output format with ``Transform(format='webp')`` or a
        :class:`~imgproxykit.options.Format` option. Omitted processing
        parameters are left to the server.

        Args:
            source: Complete source URI understood by the imgproxy server.
                The default serializer encodes its UTF-8 representation as
                URL-safe Base64 without padding. The URI is neither validated
                nor resolved against ``base_url``.
            transform: Reusable processing options and optional output format.
                Omit or pass ``None`` to add no processing options.

        Returns:
            The complete imgproxy URL, signed when credentials were supplied
            or containing the unsigned marker otherwise. No network request
            is made.
        """
        path = self._path_serializer(source, transform=transform)
        signature = self._url_signer(path)
        return f'{self._base_url}/{signature}{path}'

    def variants[Key: str](
        self,
        source: str,
        *,
        variants: Mapping[Key, Transform],
    ) -> dict[Key, str]:
        """
        Build named URLs for one source using complete transformations.

        Args:
            source: Complete source URI understood by the imgproxy server.
            variants: Names mapped to the transformation for each variant.
                Each transformation is passed unchanged to :meth:`url`.

        Returns:
            A new dictionary preserving the input keys and iteration order.
            The key type is preserved, including literal string unions.
            An empty mapping produces an empty dictionary.
            No network request is made.

        """
        return {
            name: self.url(source, transform=transform)
            for name, transform in variants.items()
        }
