from dataclasses import dataclass
from typing import ClassVar

from imgproxykit.options.base import ScalarOption


@dataclass(frozen=True, slots=True)
class Expires(ScalarOption[int]):
    """
    Reject the URL after the given Unix timestamp.

    imgproxy returns HTTP 404 after the supplied timestamp has expired.

    Attributes:
        value: Expiration time as a Unix timestamp in seconds.

    See `imgproxy expires
    <https://docs.imgproxy.net/usage/processing#expires>`_.
    """

    # TODO: Accept timezone-aware datetime objects and convert them to Unix
    # timestamps. Consider timedelta for relative expiry, resolved once at
    # construction so reusing a Transform produces a stable URL. Define how
    # naive datetimes and subsecond precision are handled.
    name: ClassVar[str] = 'expires'
    short_name: ClassVar[str | None] = 'exp'
