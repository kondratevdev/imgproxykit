from dataclasses import dataclass
from typing import ClassVar

import pytest

from imgproxykit import Transform
from imgproxykit.options import Quality, ScalarOption


def test_unknown_scalar_option() -> None:
    """Ensure that unknown scalar keywords fail with a descriptive error."""
    with pytest.raises(
        TypeError,
        match="Unknown scalar processing option 'unknown'",
    ):
        ScalarOption.from_kwarg('unknown', value=True)


def test_inherited_subclass_does_not_replace_registered_option() -> None:
    """Ensure defining subclass does not implicitly replace option."""

    @dataclass(frozen=True, slots=True)
    class StrictQuality(Quality):
        def validate(self) -> None:
            if self.value > 50:
                raise ValueError('custom restriction')

    # Instantiating StrictQuality directly applies its custom validator
    with pytest.raises(ValueError, match='custom restriction'):
        StrictQuality(80)

    # Transform(quality=80) continues to use the built-in Quality option
    transform = Transform(quality=80)
    assert type(transform.options[0]) is Quality
    assert transform.options[0].value == 80


def test_explicit_replace_updates_registry() -> None:
    """Ensure explicit replace=True replaces registered option in Transform."""

    @dataclass(frozen=True, slots=True)
    class CustomQuality(Quality, replace=True):
        pass

    try:
        transform = Transform(quality=80)
        assert type(transform.options[0]) is CustomQuality
    finally:
        # Restore original Quality registration
        ScalarOption._registry['quality'] = Quality


def test_custom_new_scalar_option_registration() -> None:
    """Ensure new scalar option is registered and usable in from_kwarg."""

    @dataclass(frozen=True, slots=True)
    class CustomScalar(ScalarOption[int]):
        name: ClassVar[str] = 'custom-scalar-test'

    try:
        opt = ScalarOption.from_kwarg('custom_scalar_test', 42)
        assert isinstance(opt, CustomScalar)
        assert opt.value == 42
    finally:
        ScalarOption._registry.pop('custom_scalar_test', None)


def test_conflicting_custom_option_name_raises_value_error() -> None:
    """Ensure conflicting custom option names raise error without replace."""
    expected_msg = (
        r"Scalar option keyword 'quality' is already registered by Quality\. "
        r'Pass replace=True to override it\.'
    )
    with pytest.raises(ValueError, match=expected_msg):

        class ConflictingOption(ScalarOption[int]):
            name: ClassVar[str] = 'quality'
