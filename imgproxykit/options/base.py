from abc import ABC, abstractmethod
from typing import ClassVar

from imgproxykit.types import Argument, OptionType


class Option(ABC):
    """
    Base class for typed imgproxy processing options.

    Concrete options provide a fixed name and positional arguments.
    Pass their instances to :class:`~imgproxykit.Transform`.
    This abstract class cannot be instantiated directly.

    Arguments retain :data:`~imgproxykit.types.EMPTY` values until
    serialization: internal gaps keep their positions, while trailing
    empty arguments are omitted.

    See `imgproxy processing options
    <https://docs.imgproxy.net/usage/processing#processing-options>`_.

    """

    __slots__ = ()

    # TODO: Validate server-independent option constraints at construction
    # time (for example, rotation multiples of 90 and positive DPR/zoom).
    # Raise ValueError with the option name and violated constraint.
    # Leave configuration-dependent restrictions to the imgproxy server.
    # TODO: Allow custom option names without type ignores; decide whether
    # Option.name should return str, keeping OptionType for built-in names.
    # TODO: Unify constructors: Quality and DPR allow positional values,
    # while other single-value options require keywords. Allow positional
    # scalar values consistently (for example, Blur(2) and Rotate(90)),
    # keeping multi-argument options keyword-only.

    # Private API:
    _name: ClassVar[OptionType]

    @property
    def name(self) -> OptionType:
        """The fixed imgproxy processing option name."""
        return self._name

    @property
    @abstractmethod
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
