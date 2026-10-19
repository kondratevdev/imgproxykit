from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.internal.encoding import encode_base64
from imgproxykit.options.base import ScalarOption
from imgproxykit.types import Argument, OptionType


@dataclass(frozen=True, slots=True)
class Filename(ScalarOption[str]):
    """
    Set the response filename using URL-safe Base64 encoding.

    Sets the filename in the Content-Disposition response header.
    The name is encoded as URL-safe Base64 automatically. Combine with
    ReturnAttachment to request downloading in the browser.

    Attributes:
        value: Response filename, supplied as unencoded text.

    Usage:

    >>> option = Filename('product photo.jpg')
    >>> option.arguments
    ('cHJvZHVjdCBwaG90by5qcGc', True)

    See `imgproxy filename
    <https://docs.imgproxy.net/usage/processing#filename>`_.

    """

    name: ClassVar[OptionType] = 'filename'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (encode_base64(self.value), True)
