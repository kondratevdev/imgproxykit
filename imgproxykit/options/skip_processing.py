from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, FormatType


@dataclass(frozen=True, slots=True, kw_only=True)
class SkipProcessing(Option):
    """
    Skip processing listed formats when source and output formats match.

    Processing is skipped only when the requested output format matches
    the source format. Video thumbnail processing cannot be skipped.

    Attributes:
        formats: Source formats eligible for skipping processing.

    Usage:

    >>> option = SkipProcessing(formats=('svg', 'gif'))
    >>> option.arguments
    ('svg', 'gif')

    See `imgproxy skip processing
    <https://docs.imgproxy.net/usage/processing#skip-processing>`_.

    """

    formats: tuple[FormatType, ...]

    name: ClassVar[str] = 'skip_processing'
    short_name: ClassVar[str | None] = 'skp'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return self.formats
