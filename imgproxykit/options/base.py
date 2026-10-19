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

    # Public API:
    name: ClassVar[OptionType]
    """
    All subtypes must provide a supported imgproxy processing option name.

    The name is shared by all instances and is not a dataclass field
    or a constructor argument.
    """

    def __post_init__(self) -> None:
        """Validate option arguments at construction time."""
        self.validate()

    def validate(self) -> None:  # noqa: B027
        """
        Validate option arguments.

        Override this method to enforce server-independent constraints.
        The default implementation does nothing.

        Raises:
            ValueError: If option arguments are invalid.

        """

    @property
    @abstractmethod
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
