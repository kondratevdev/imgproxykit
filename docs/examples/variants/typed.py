"""
Preserve literal key types in generated URL dictionaries.

>>> list(product_urls)
['small', 'medium', 'large']
>>> list(avatar_urls)
['thumbnail', 'profile']
"""

from typing import Literal, assert_type

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

type ProductKeys = Literal['small', 'medium', 'large']
type AvatarKeys = Literal['thumbnail', 'profile']

base = Transform(quality=85, format='webp')

# start-typed-products
products: dict[ProductKeys, Transform] = {
    'small': Transform(*base.options, width=320),
    'medium': Transform(*base.options, width=640),
    'large': Transform(*base.options, width=1280),
}
# end-typed-products

avatars: dict[AvatarKeys, Transform] = {
    'thumbnail': Transform(
        *base.options,
        Resize(width=48, height=48, mode='fill'),
    ),
    'profile': Transform(
        *base.options,
        Resize(width=192, height=192, mode='fill'),
    ),
}

client = Client('https://imgproxy.example.com')
product_urls = client.variants(
    'https://originals.example.com/product.jpg',
    variants=products,
)
avatar_urls = client.variants(
    'https://originals.example.com/avatar.jpg',
    variants=avatars,
)

assert_type(product_urls, dict[ProductKeys, str])
assert_type(avatar_urls, dict[AvatarKeys, str])
