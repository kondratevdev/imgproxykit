"""
Preserve literal key types in generated URL dictionaries.

>>> list(product_urls)
['small', 'medium', 'large']
"""

from typing import Literal, assert_type

from imgproxykit import Client, Transform

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Limit the allowed variant names with a literal union.
type ProductKeys = Literal['small', 'medium', 'large']

products: dict[ProductKeys, Transform] = {
    'small': Transform(width=320),
    'medium': Transform(width=640),
    'large': Transform(width=1280),
}

# The returned dictionary preserves the annotated key type.
product_urls = client.variants(source=source_url, variants=products)
assert_type(product_urls, dict[ProductKeys, str])

print(product_urls['small'])
