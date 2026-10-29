from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class MaxSrcFileSize(ScalarOption[int]):
    """
    Override source byte limit; requires ALLOW_SECURITY_OPTIONS.

    Overrides the corresponding server limit for this request. Requires
    `IMGPROXY_ALLOW_SECURITY_OPTIONS
    <https://docs.imgproxy.net/latest/configuration/options#security>`__
    set to ``true`` on the imgproxy server.

    Attributes:
        value: Source file size limit in bytes.

    Usage:

    >>> option = MaxSrcFileSize(10_000_000)
    >>> option.arguments
    (10000000,)

    See `imgproxy max src file size
    <https://docs.imgproxy.net/usage/processing#max-src-file-size>`_.

    """

    name: ClassVar[str] = 'max_src_file_size'
    short_name: ClassVar[str | None] = 'msfs'
