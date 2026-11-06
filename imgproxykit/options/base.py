from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.types import Argument


class Option(ABC):
    """
    Base class for typed imgproxy processing options.

    Concrete options provide a fixed name and positional arguments.
    Pass their instances to :class:`~imgproxykit.Transform`.
    This abstract class cannot be instantiated directly.

    Arguments retain ``None`` values until
    serialization: internal gaps keep their positions, while trailing
    ``None`` values are omitted. Other false values (such as empty
    strings, zeroes, and ``False``) keep their positions.

    See `imgproxy processing options
    <https://docs.imgproxy.net/usage/processing#processing-options>`_.
    """

    __slots__ = ()

    # Public API:
    name: ClassVar[str]
    """
    All subtypes must provide a supported imgproxy processing option name.

    The name is shared by all instances and is not a dataclass field
    or a constructor argument.
    """

    short_name: ClassVar[str | None] = None
    """
    Shortest documented imgproxy alias, or ``None`` if none is available.

    Like ``name``, this is shared by instances and is not a constructor
    argument. Use ``name`` when no short alias is defined.
    """

    @property
    @abstractmethod
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""


@dataclass(frozen=True, slots=True)
class ScalarOption[ValueT: Argument](Option):
    """
    Base class for processing options accepting one scalar value.

    Concrete subclasses specify the value type and processing option name.
    Override :attr:`arguments` when the option requires custom encoding.

    Attributes:
        value: Scalar processing option value.
    """

    value: ValueT

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
