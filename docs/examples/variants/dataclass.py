from dataclasses import dataclass
from pprint import pprint
from typing import Annotated, assert_type

from imgproxykit import Client, Transform

base = Transform(quality=85, format='webp')


@dataclass(frozen=True, slots=True)
class ProductImages:
    """Declare the result fields and their transformations together."""

    small: Annotated[str, base.extend(width=320)]  # (1)!
    medium: Annotated[str, base.extend(width=640)]
    large: Annotated[str, base.extend(width=1280)]


client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

product_urls = client.variants(source_url, variants=ProductImages)  # (2)!

assert_type(product_urls, ProductImages)
assert_type(product_urls.small, str)

pprint(product_urls)
