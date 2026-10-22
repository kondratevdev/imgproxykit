"""
Build a reusable set of product variants.

>>> list(product_urls)
['small', 'medium', 'large']
>>> small_url == client.url(source_url, transform=products['small'])
True
"""

from imgproxykit import Client, Transform

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'
# Share quality and output format across all variants.
base = Transform(quality=85, format='webp')

products = {
    # Unpack shared options and add a width for each variant.
    'small': Transform(*base.options, width=320),
    'medium': Transform(*base.options, width=640),
    'large': Transform(*base.options, width=1280),
}
product_urls = client.variants(source=source_url, variants=products)
small_url = product_urls['small']  # Access a URL by its variant name.
