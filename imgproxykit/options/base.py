from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, ClassVar, override

from imgproxykit.types import Argument


class Option(ABC):
    """
    Base class for typed imgproxy processing options.

    Concrete options provide a fixed name and positional arguments.
    Pass their instances to :class:`~imgproxykit.Transform`.
    This abstract class cannot be instantiated directly.

    Arguments retain ``None`` values until
    serialization: internal gaps keep their positions, while trailing
    empty arguments are omitted.

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
        # TODO: Add per option validation

    @property
    @abstractmethod
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""


type _ScalarRegistry = dict[str, type[ScalarOption[Any]]]


@dataclass(frozen=True, slots=True)
class ScalarOption[ValueT: Argument](Option):
    """
    Base class for processing options accepting one scalar value.

    Subclasses are registered automatically using their processing option
    name, with hyphens replaced by underscores. This allows passing scalar
    values directly to :class:`~imgproxykit.Transform` as keyword arguments.

    Concrete subclasses specify the value type and processing option name.
    Override :attr:`arguments` when the option requires custom encoding.

    Attributes:
        value: Scalar processing option value.

    """

    value: ValueT

    _registry: ClassVar[_ScalarRegistry] = {}

    @override
    def __init_subclass__(cls, *, replace: bool = False, **kwargs: Any) -> None:
        """Register a concrete scalar option for keyword construction."""
        # Explicit super is required because slots=True replaces this class.
        super(ScalarOption, cls).__init_subclass__(**kwargs)  # noqa: WPS608
        kwarg_name = cls._get_kwarg_name()
        existing = ScalarOption._registry.get(kwarg_name)
        if existing is not None and not replace:
            # Slotted dataclasses create a replacement class with the exact
            # same name and module. Allow this re-registration so keyword
            # construction uses the final class, including its slots.
            is_same_class = (
                cls.__name__ == existing.__name__
                and cls.__module__ == existing.__module__
            )
            if is_same_class:
                ScalarOption._registry[kwarg_name] = cls
                return
            # Subclasses inheriting the option name do not replace the existing
            # registration.
            if issubclass(cls, existing):
                return
            raise ValueError(
                f'Scalar option keyword {kwarg_name!r} is already registered '
                f'by {existing.__name__}. Pass replace=True to override it.',
            )
        ScalarOption._registry[kwarg_name] = cls

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)

    @classmethod
    def from_kwarg(cls, name: str, value: Argument) -> 'ScalarOption[Any]':
        """
        Construct a registered scalar option from a Transform keyword.

        The concrete option constructor handles value validation and
        protocol-specific encoding, just as with positional options.

        Args:
            name: Python keyword name of a registered scalar option.
            value: Value passed to the concrete option constructor.

        Raises:
            TypeError: If the keyword does not identify a scalar option.
            ValueError: If the concrete option rejects the supplied value.

        """
        option_cls = cls._registry.get(name)
        if option_cls is None:
            raise TypeError(
                f'Unknown scalar processing option {name!r}. '
                'Transform keyword arguments must name a registered scalar '
                'option. '
                'Pass complex processing options as positional Option '
                'instances.',
            )
        return option_cls(value)

    @classmethod
    def _get_kwarg_name(cls) -> str:
        """Convert the processing option name to its Python keyword name."""
        return cls.name.replace('-', '_')
