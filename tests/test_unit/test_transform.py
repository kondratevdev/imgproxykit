from dataclasses import dataclass
from typing import ClassVar

import pytest

from imgproxykit import Transform
from imgproxykit.options import (
    DPR,
    Format,
    Quality,
    Resize,
    ScalarOption,
    Width,
)


@dataclass(frozen=True, slots=True)
class _CustomWidth(ScalarOption[int]):
    """A positional option with the same URL name as Width."""

    name: ClassVar[str] = 'width'


@dataclass(frozen=True, slots=True)
class _ColorBoost(ScalarOption[int]):
    """Declare a custom option with a unique name."""

    name: ClassVar[str] = 'color_boost'


def test_extend() -> None:
    """Retain option order and duplicates without changing the original."""
    base = Transform(quality=85, format='webp')
    extended = base.extend(Resize(width=300), quality=70, dpr=2)

    assert extended.options == (
        Quality(85),
        Format('webp'),
        Resize(width=300),
        Quality(70),
        DPR(2),
    )
    assert base.options == (Quality(85), Format('webp'))


def test_extend_without_options() -> None:
    """Return an equal but distinct transform when no options are added."""
    base = Transform(quality=85, format='webp')
    extended = base.extend()

    assert extended == base
    assert extended is not base


def test_custom_option_name_collision() -> None:
    """Keep the built-in keyword when a custom option shares its name."""
    custom = _CustomWidth(100)
    transform = Transform(custom, width=800)

    assert transform.options == (custom, Width(800))


def test_custom_option_rejects_keyword() -> None:
    """Accept a custom option instance and reject its name as a keyword."""
    custom = _ColorBoost(25)
    assert Transform(custom).options == (custom,)

    with pytest.raises(
        TypeError,
        match="Unknown scalar processing option 'color_boost'",
    ):
        Transform(  # type: ignore[call-arg]
            color_boost=25,  # pyright: ignore[reportCallIssue]  # ty: ignore[unknown-argument]  # pyrefly: ignore[unexpected-keyword]
        )
