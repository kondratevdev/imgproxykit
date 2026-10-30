from datetime import UTC, datetime, timedelta

import pytest

from imgproxykit import Transform
from imgproxykit.options import Expires
from imgproxykit.serialization import PathSerializer


def test_expires_int(path_serializer: PathSerializer) -> None:
    """Ensure that integer timestamps are serialized directly."""
    option = Expires(1700000000)
    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == 'expires:1700000000'
    )


def test_expires_datetime(path_serializer: PathSerializer) -> None:
    """Ensure that timezone-aware datetimes are converted to timestamps."""
    target = datetime(2026, 1, 1, 12, 0, 0, tzinfo=UTC)
    expected_ts = int(target.timestamp())
    option = Expires(target)

    assert (
        path_serializer._serialize_segment(option.name, option.arguments)
        == f'expires:{expected_ts}'
    )


def test_expires_timedelta(path_serializer: PathSerializer) -> None:
    """Ensure that timedelta resolves relative to current time."""
    before = int(datetime.now(tz=UTC).timestamp())
    option = Expires(timedelta(hours=1))
    segment = path_serializer._serialize_segment(option.name, option.arguments)
    after = int(datetime.now(tz=UTC).timestamp())

    assert segment.startswith('expires:')
    resolved_ts = int(segment.removeprefix('expires:'))
    assert before + 3600 <= resolved_ts <= after + 3600


def test_expires_transform_keyword(path_serializer: PathSerializer) -> None:
    """Ensure that Transform accepts timedelta and datetime keywords."""
    target = datetime(2026, 6, 1, tzinfo=UTC)
    transform = Transform(expires=target)

    assert len(transform.options) == 1
    assert (
        path_serializer._serialize_segment(
            transform.options[0].name,
            transform.options[0].arguments,
        )
        == f'expires:{int(target.timestamp())}'
    )


def test_expires_naive_datetime_rejected() -> None:
    """Ensure that naive datetime values raise ValueError."""
    naive_dt = datetime(2026, 1, 1, 12, 0, 0)  # noqa: DTZ001
    with pytest.raises(
        ValueError,
        match='Naive datetime values are not accepted',
    ):
        Expires(naive_dt)


def test_expires_negative_int_rejected() -> None:
    """Ensure that negative integers raise ValueError."""
    with pytest.raises(
        ValueError,
        match='Expiration timestamp cannot be negative',
    ):
        Expires(-1)


def test_expires_negative_timedelta_rejected() -> None:
    """Ensure that negative timedeltas raise ValueError."""
    with pytest.raises(
        ValueError,
        match='Expiration timedelta cannot be negative',
    ):
        Expires(timedelta(seconds=-1))


def test_expires_negative_datetime_rejected() -> None:
    """Ensure that pre-epoch datetimes raise ValueError."""
    pre_epoch = datetime(1960, 1, 1, tzinfo=UTC)
    with pytest.raises(
        ValueError,
        match='Expiration timestamp cannot be negative',
    ):
        Expires(pre_epoch)


@pytest.mark.parametrize('bool_val', [True, False])
def test_expires_boolean_rejected(*, bool_val: bool) -> None:
    """Ensure that booleans raise TypeError."""
    with pytest.raises(TypeError, match='Expires value cannot be a boolean'):
        Expires(bool_val)  # type: ignore[arg-type]


def test_expires_invalid_type_rejected() -> None:
    """Ensure that unsupported types raise TypeError."""
    with pytest.raises(TypeError, match='Expires value must be int'):
        Expires('not-a-timestamp')  # type: ignore[arg-type]
