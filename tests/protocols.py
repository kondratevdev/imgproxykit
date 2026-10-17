from typing import Protocol

from imgproxykit.options import Option


class OptionFactory[Value](Protocol):
    """Construct a scalar option through its keyword-only value."""

    def __call__(self, *, value: Value) -> Option:
        """Build an option with the supplied value."""
        ...
