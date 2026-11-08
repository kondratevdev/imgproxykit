import pytest

from imgproxykit.transform import KeywordOptionResolver


def test_unknown_scalar_option() -> None:
    """Ensure that unknown scalar keywords fail with a descriptive error."""
    with pytest.raises(
        TypeError,
        match="Unknown scalar processing option 'unknown'",
    ):
        KeywordOptionResolver.from_kwarg('unknown', value=True)
