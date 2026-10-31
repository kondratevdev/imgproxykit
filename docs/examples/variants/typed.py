from pprint import pprint
from typing import Literal, assert_type

from imgproxykit import Client, Transform

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

type ProductKeys = Literal['small', 'medium', 'large']  # (1)!

products: dict[ProductKeys, Transform] = {
    'small': Transform(width=320),
    'medium': Transform(width=640),
    'large': Transform(width=1280),
}

product_urls = client.variants(source=source_url, variants=products)
assert_type(product_urls, dict[ProductKeys, str])  # (2)!

pprint(product_urls, sort_dicts=False)
