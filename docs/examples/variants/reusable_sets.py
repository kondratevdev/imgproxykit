"""
Reuse shared settings across product and avatar collections.

>>> list(product_urls)
['small', 'medium', 'large']
>>> list(avatar_urls)
['thumbnail', 'profile']
>>> product_urls['small'] != another_product_urls['small']
True
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

# Share quality and output format across both sets.
base = Transform(quality=85, format='webp')

products = {
    # Add dimensions to the shared options for each variant.
    'small': Transform(*base.options, width=320),
    'medium': Transform(*base.options, width=640),
    'large': Transform(*base.options, width=1280),
}

avatars = {
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
another_product_urls = client.variants(
    'https://originals.example.com/another-product.jpg',
    variants=products,
)
avatar_urls = client.variants(
    'https://originals.example.com/avatar.jpg',
    variants=avatars,
)
