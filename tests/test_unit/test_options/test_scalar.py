import types
from dataclasses import dataclass
from typing import override

import pytest

from imgproxykit import Transform
from imgproxykit.options import Quality, ScalarOption


@dataclass(frozen=True, slots=True)
class _StrictQuality(Quality):
    """Subclass without replace for test."""

    @override
    def validate(self) -> None:
        """Validate value bound."""
        if self.value > 50:
            raise ValueError('custom restriction')


def _set_custom_name(namespace: dict[str, object]) -> None:
    """Set custom scalar name in namespace."""
    namespace['name'] = 'custom-scalar-test'


def _set_conflict_name(namespace: dict[str, object]) -> None:
    """Set conflicting scalar name in namespace."""
    namespace['name'] = 'quality'


def test_unknown_scalar_option() -> None:
    """Ensure that unknown scalar keywords fail with a descriptive error."""
    with pytest.raises(
        TypeError,
        match="Unknown scalar processing option 'unknown'",
    ):
        ScalarOption.from_kwarg('unknown', value=True)


def test_subclass_does_not_replace_option() -> None:
    """Ensure defining subclass does not implicitly replace option."""
    with pytest.raises(ValueError, match='custom restriction'):
        _StrictQuality(80)

    transform = Transform(quality=80)
    assert transform.options[0].__class__ is Quality
    assert transform.options[0].value == 80


def test_explicit_replace_updates_registry(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Ensure explicit replace=True replaces registered option in Transform."""
    monkeypatch.setitem(ScalarOption._registry, 'quality', Quality)
    custom = types.new_class('CustomQuality', (Quality,), {'replace': True})

    transform = Transform(quality=80)
    assert transform.options[0].__class__ is custom


def test_custom_scalar_options(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure custom option registration and conflict prevention work."""
    monkeypatch.delitem(
        ScalarOption._registry,
        'custom_scalar_test',
        raising=False,
    )
    custom = types.new_class(
        'CustomScalar',
        (ScalarOption[int],),
        exec_body=_set_custom_name,
    )
    opt = ScalarOption.from_kwarg('custom_scalar_test', 42)
    assert opt.__class__ is custom
    assert opt.value == 42

    expected_msg = (
        r"Scalar option keyword 'quality' is already registered by Quality\. "
        r'Pass replace=True to override it\.'
    )
    with pytest.raises(ValueError, match=expected_msg):
        types.new_class(
            'ConflictingOption',
            (ScalarOption[int],),
            exec_body=_set_conflict_name,
        )
