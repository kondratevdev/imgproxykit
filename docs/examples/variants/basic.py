"""
Generate named variant URLs for one source.

>>> list(product_urls)
['small', 'medium', 'large']
>>> small_url == client.url(source_url, transform=products['small'])
True
"""

from imgproxykit import Client, Transform

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Define a complete transformation for each variant name.
products = {
    'small': Transform(width=320),
    'medium': Transform(width=640),
    'large': Transform(width=1280),
}

# Build one URL per variant for the same source image.
product_urls = client.variants(source=source_url, variants=products)
small_url = product_urls['small']  # Access a URL by its variant name.

print(small_url)
