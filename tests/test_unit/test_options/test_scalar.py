import pytest

from imgproxykit.options import ScalarOption


def test_unknown_scalar_option() -> None:
    """Ensure that unknown scalar keywords fail with a descriptive error."""
    with pytest.raises(
        TypeError,
        match="Unknown scalar processing option 'unknown'",
    ):
        ScalarOption.from_kwarg('unknown', value=True)
