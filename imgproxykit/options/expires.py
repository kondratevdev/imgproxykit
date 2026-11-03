from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from math import floor
from typing import ClassVar, Self

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

    name: ClassVar[str] = 'expires'
    short_name: ClassVar[str | None] = 'exp'

    @classmethod
    def at(cls, deadline: datetime) -> Self:
        """
        Create an expiration from a timezone-aware datetime.

        Subsecond precision is rounded down to whole Unix seconds.
        Past deadlines are accepted.

        Raises:
            ValueError: If the deadline is a naive datetime.
        """
        if deadline.utcoffset() is None:
            raise ValueError('Expiration deadline must be timezone-aware')

        return cls(floor(deadline.timestamp()))

    @classmethod
    def after(cls, ttl: timedelta) -> Self:
        """
        Create an expiration relative to the current time.

        The deadline is fixed when this method is called. Reusing the option
        does not renew it. Subsecond precision is rounded down, so a TTL
        shorter than one second may expire immediately.

        Raises:
            ValueError: If the TTL is not positive.
        """
        if ttl <= timedelta(0):
            raise ValueError('Expiration TTL must be positive')

        return cls.at(datetime.now(UTC) + ttl)
