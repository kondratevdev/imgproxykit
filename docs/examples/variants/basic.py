"""
Generate variant URLs for one source.

>>> list(product_urls)
['small', 'medium', 'large']
>>> product_urls['small'] == client.url(source_url, transform=products['small'])
True
"""

from imgproxykit import Client, Transform

products = {
    'small': Transform(width=320),
    'medium': Transform(width=640),
    'large': Transform(width=1280),
}

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/product.jpg'
product_urls = client.variants(source_url, variants=products)
small_url = product_urls['small']  # Access a URL by its variant name.
