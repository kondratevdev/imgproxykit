from dataclasses import dataclass
from itertools import starmap
from typing import ClassVar, Unpack

from imgproxykit.keyword_options import KeywordOptionResolver, KeywordOptions
from imgproxykit.options import Option


@dataclass(frozen=True, slots=True, init=False)
class Transform:
    """
    Define reusable image processing options.

    Stores an immutable tuple of options for reuse with
    :meth:`imgproxykit.Client.url`. Pass option instances or scalar keyword
    arguments; scalar options follow the positional options in keyword order.
    Use :meth:`extend` to create a new transformation with additional options
    without changing the original.

    Options retain their supplied order during serialization. Imgproxy
    determines the image processing pipeline and resolves omitted arguments
    using its defaults. Preset options reference names configured on the
    imgproxy server and are not expanded here.

    Attributes:
        options: Tuple of processing options. Defaults to an empty tuple,
            which adds no processing option segments to the URL.
    """

    #: Component that resolves built-in scalar keyword options.
    keyword_option_resolver_cls: ClassVar[type[KeywordOptionResolver]] = (
        KeywordOptionResolver
    )

    options: tuple[Option, ...]

    def __init__(
        self,
        *options: Option,
        **kwargs: Unpack[KeywordOptions],
    ) -> None:
        """
        Collect positional options, followed by scalar keyword options.

        Args:
            *options: Processing option instances in serialization order.
                Repeated options are retained without merging.
            **kwargs: Scalar processing arguments, such as ``quality=85``
                or ``format='webp'``. Converted to option instances and
                appended in keyword order.
        """
        # Keep variadic options while initializing a frozen dataclass.
        # Bypassing __setattr__ is safe until initialization is finished.
        scalar_options = tuple(
            starmap(
                self.keyword_option_resolver_cls.from_kwarg,
                kwargs.items(),
            ),
        )
        object.__setattr__(self, 'options', (*options, *scalar_options))

    def extend(
        self,
        *options: Option,
        **kwargs: Unpack[KeywordOptions],
    ) -> 'Transform':
        """
        Return a new transformation with additional processing options.

        The original transformation remains unchanged. Existing options are
        followed by positional options, then scalar keyword options in keyword
        order. Repeated options are retained without merging or replacing them.

        Args:
            *options: Processing option instances in serialization order.
                Repeated options are retained without merging.
            **kwargs: Scalar processing arguments, such as ``quality=85``
                or ``format='webp'``. Converted to option instances and
                appended in keyword order.
        """
        return type(self)(*self.options, *options, **kwargs)
