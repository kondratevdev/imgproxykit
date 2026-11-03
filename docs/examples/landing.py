from dataclasses import dataclass
from pprint import pprint
from typing import Annotated

from imgproxykit import Client, Transform

base = Transform(  # (1)!
    format='webp',
    quality=85,
    enlarge=False,
)


@dataclass(frozen=True)
class ImageVariants:
    """Declare named image URLs and their transformations."""

    thumbnail: Annotated[str, base.extend(width=300)]  # (2)!
    preview: Annotated[str, base.extend(width=1200)]
    original: Annotated[str, Transform(raw=True)]  # (3)!


client = Client('https://imgproxy.example.com')  # (4)!
images = client.variants(
    source='https://originals.example.com/photo.jpg',  # (5)!
    variants=ImageVariants,  # (6)!
)

pprint(images)
