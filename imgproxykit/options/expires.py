from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import ClassVar, override

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True)
class Expires(ScalarOption[int | datetime | timedelta]):
    """
    Reject the URL after the given Unix timestamp or duration.

    imgproxy returns HTTP 404 after the supplied timestamp has expired.

    Attributes:
        value: Expiration time as an integer Unix timestamp in seconds, a
            timezone-aware :class:`~datetime.datetime`, or a relative
            :class:`~datetime.timedelta`.

    Notes:
        When initialized with a :class:`~datetime.timedelta`, the expiration
        timestamp is resolved dynamically when serializing the option (building
        the URL), allowing a :class:`~imgproxykit.Transform` to be reused
        across multiple URL generations.

        Naive :class:`~datetime.datetime` objects are rejected with
        :exc:`ValueError` to prevent timezone ambiguity.

    See `imgproxy expires
    <https://docs.imgproxy.net/usage/processing#expires>`_.

    """

    name: ClassVar[str] = 'expires'
    short_name: ClassVar[str | None] = 'exp'

    @override
    def validate(self) -> None:
        """
        Validate expiration time.

        Raises:
            TypeError: If ``value`` is a boolean or not an accepted type.
            ValueError: If ``value`` is negative or a naive datetime.

        """
        if isinstance(self.value, bool):
            raise TypeError('Expires value cannot be a boolean.')
        if isinstance(self.value, datetime):
            self._validate_datetime(self.value)
        elif isinstance(self.value, timedelta):
            self._validate_timedelta(self.value)
        elif isinstance(self.value, int):  # pyright: ignore[reportUnnecessaryIsInstance]
            self._validate_int(self.value)
        else:
            raise TypeError(
                f'Expires value must be int, datetime, or timedelta, '
                f'got {type(self.value).__name__}.',
            )

    @staticmethod
    def _validate_datetime(value: datetime) -> None:
        if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
            raise ValueError(
                'Naive datetime values are not accepted; provide a '
                'timezone-aware datetime.',
            )
        if value.timestamp() < 0:
            raise ValueError('Expiration timestamp cannot be negative.')

    @staticmethod
    def _validate_timedelta(value: timedelta) -> None:
        if value.total_seconds() < 0:
            raise ValueError('Expiration timedelta cannot be negative.')

    @staticmethod
    def _validate_int(value: int) -> None:
        if value < 0:
            raise ValueError('Expiration timestamp cannot be negative.')

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        if isinstance(self.value, timedelta):
            expires_at = datetime.now(tz=UTC) + self.value
            return (int(expires_at.timestamp()),)
        if isinstance(self.value, datetime):
            return (int(self.value.timestamp()),)
        return (self.value,)
