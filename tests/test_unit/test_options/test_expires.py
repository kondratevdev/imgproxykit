from datetime import UTC, datetime, timedelta, timezone
from typing import Final

import pytest
import time_machine

from imgproxykit.options import Expires

_FROZEN_TIME: Final = '2026-01-01T00:00:00.750000+00:00'
_TIMESTAMP: Final = 1767225600


@pytest.mark.parametrize(
    ('deadline', 'expected'),
    [
        # UTC deadlines are converted to Unix seconds.
        (datetime(2026, 1, 1, tzinfo=UTC), _TIMESTAMP),
        # The same instant in another time zone gives the same timestamp.
        (
            datetime(2026, 1, 1, 5, tzinfo=timezone(timedelta(hours=5))),
            _TIMESTAMP,
        ),
        # Fractional seconds are rounded down.
        (datetime(2026, 1, 1, microsecond=999_999, tzinfo=UTC), _TIMESTAMP),
        # Past deadlines are accepted; negative fractions round down to -1.
        (datetime(1969, 12, 31, 23, 59, 59, 500_000, tzinfo=UTC), -1),
    ],
)
def test_expires_at(*, deadline: datetime, expected: int) -> None:
    """Ensure that absolute deadlines use Unix seconds rounded down."""
    assert Expires.at(deadline) == Expires(expected)


@pytest.mark.parametrize(
    ('ttl', 'expected'),
    [
        # Whole-minute durations are added to the frozen current time.
        (timedelta(minutes=15), _TIMESTAMP + 15 * 60),
        # A short duration can expire within the current Unix second.
        (timedelta(microseconds=100_000), _TIMESTAMP),
        # Crossing a second boundary adds a second before rounding down.
        (timedelta(microseconds=500_000), _TIMESTAMP + 1),
    ],
)
@time_machine.travel(_FROZEN_TIME, tick=False)
def test_expires_after(*, ttl: timedelta, expected: int) -> None:
    """Ensure that relative deadlines add the TTL before rounding down."""
    assert Expires.after(ttl) == Expires(expected)


def test_expires_fixed_deadline() -> None:
    """Ensure that reading arguments does not renew the expiration."""
    with time_machine.travel(_FROZEN_TIME, tick=False) as traveller:
        option = Expires.after(timedelta(minutes=15))

        assert option.arguments == (_TIMESTAMP + 15 * 60,)
        # Advancing time must not renew the deadline fixed at construction.
        traveller.shift(timedelta(days=1))
        assert option.arguments == (_TIMESTAMP + 15 * 60,)


@pytest.mark.parametrize(
    'ttl',
    [
        # Zero does not provide a positive lifetime.
        timedelta(0),
        # Even a fractional negative duration is rejected.
        timedelta(microseconds=-1),
    ],
)
def test_invalid_expires_ttl(*, ttl: timedelta) -> None:
    """Ensure that zero and negative expiration durations are rejected."""
    with pytest.raises(ValueError, match='TTL must be positive'):
        Expires.after(ttl)


def test_naive_expires_deadline() -> None:
    """Ensure that absolute deadlines require a time zone."""
    with pytest.raises(ValueError, match='must be timezone-aware'):
        Expires.at(datetime(2026, 1, 1))  # noqa: DTZ001
