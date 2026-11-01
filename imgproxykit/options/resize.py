from dataclasses import dataclass
from typing import ClassVar, Self, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, ResizeType


@dataclass(frozen=True, slots=True, kw_only=True)
class Resize(Option):  # noqa: WPS214
    """
    Configure image dimensions and resizing behavior.

    Values left as ``None`` are not supplied
    explicitly; imgproxy resolves their defaults.

    Select a strategy with :meth:`fit`, :meth:`fill`, :meth:`fill_down`,
    :meth:`force`, or :meth:`auto`. Use the constructor when the mode is
    supplied dynamically or should be left to the server.

    Attributes:
        width: Target width in pixels.
        height: Target height in pixels.
        mode: Resizing strategy, such as ``fit`` or ``fill``.
        enlarge: Allow upscaling smaller source images.
        extend: Pad images that are smaller than the target dimensions.

    Usage:

    >>> option = Resize.fill(width=96, height=96)
    >>> option.arguments
    ('fill', 96, 96, None, None)
    >>> option = Resize.fit(width=300, enlarge=False)
    >>> option.arguments
    ('fit', 300, None, False, None)

    See `imgproxy resize
    <https://docs.imgproxy.net/usage/processing#resize>`_.
    """

    width: int | None = None
    height: int | None = None
    mode: ResizeType | None = None
    enlarge: bool | None = None
    extend: bool | None = None

    name: ClassVar[str] = 'resize'
    short_name: ClassVar[str | None] = 'rs'

    @classmethod
    def fit(
        cls,
        *,
        width: int | None = None,
        height: int | None = None,
        enlarge: bool | None = None,
        extend: bool | None = None,
    ) -> Self:
        """Resize using the fit strategy with optional dimensions."""
        return cls(
            mode='fit',
            width=width,
            height=height,
            enlarge=enlarge,
            extend=extend,
        )

    @classmethod
    def fill(
        cls,
        *,
        width: int | None = None,
        height: int | None = None,
        enlarge: bool | None = None,
        extend: bool | None = None,
    ) -> Self:
        """Resize using the fill strategy with optional dimensions."""
        return cls(
            mode='fill',
            width=width,
            height=height,
            enlarge=enlarge,
            extend=extend,
        )

    @classmethod
    def fill_down(
        cls,
        *,
        width: int | None = None,
        height: int | None = None,
        enlarge: bool | None = None,
        extend: bool | None = None,
    ) -> Self:
        """Resize using the fill-down strategy with optional dimensions."""
        return cls(
            mode='fill-down',
            width=width,
            height=height,
            enlarge=enlarge,
            extend=extend,
        )

    @classmethod
    def force(
        cls,
        *,
        width: int | None = None,
        height: int | None = None,
        enlarge: bool | None = None,
        extend: bool | None = None,
    ) -> Self:
        """Resize using the force strategy with optional dimensions."""
        return cls(
            mode='force',
            width=width,
            height=height,
            enlarge=enlarge,
            extend=extend,
        )

    @classmethod
    def auto(
        cls,
        *,
        width: int | None = None,
        height: int | None = None,
        enlarge: bool | None = None,
        extend: bool | None = None,
    ) -> Self:
        """Resize using the auto strategy with optional dimensions."""
        return cls(
            mode='auto',
            width=width,
            height=height,
            enlarge=enlarge,
            extend=extend,
        )

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.mode,
            self.width,
            self.height,
            self.enlarge,
            self.extend,
        )
