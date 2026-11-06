from dataclasses import dataclass
from typing import ClassVar, override

from imgproxykit import Client, Transform
from imgproxykit.options import Option, ScalarOption
from imgproxykit.types import Argument


@dataclass(frozen=True, slots=True)
class ColorBoost(ScalarOption[int]):  # (1)!
    """Set the color boost strength."""

    name: ClassVar[str] = 'color_boost'


@dataclass(frozen=True, slots=True, kw_only=True)
class Border(Option):  # (2)!
    """Set the border width and color."""

    name: ClassVar[str] = 'border'
    width: int
    color: str

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        return (self.width, self.color)


client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

transform = Transform(ColorBoost(25), width=800)  # (3)!
framed = transform.extend(Border(width=4, color='ffffff'))

image_url = client.url(source=source_url, transform=framed)

print(image_url)
