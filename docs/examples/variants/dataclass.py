"""
Return a typed dataclass instance with named URL attributes.

>>> isinstance(product_urls, ProductImages)
True
>>> product_urls.small.startswith(
...     'http://localhost:8080/unsafe/quality:85/format:webp/width:320/'
... )
True
"""

from dataclasses import dataclass
from typing import Annotated, assert_type

from imgproxykit import Client, Transform

# Share processing settings across all variants.
base = Transform(quality=85, format='webp')


@dataclass(frozen=True, slots=True)
class ProductImages:
    """Declare the result fields and their transformations together."""

    small: Annotated[str, base.extend(width=320)]
    medium: Annotated[str, base.extend(width=640)]
    large: Annotated[str, base.extend(width=1280)]


client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Pass the class to build an instance containing the generated URLs.
product_urls = client.variants(source_url, variants=ProductImages)

assert_type(product_urls, ProductImages)
assert_type(product_urls.small, str)

print(product_urls.small)
