"""
Build a reusable set of product variants.

>>> list(product_urls)
['small', 'medium', 'large']
>>> product_urls['small'] == client.url(source_url, transform=products['small'])
True
"""

from imgproxykit import Client, Transform

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Share quality and output format across all variants.
base = Transform(quality=85, format='webp')
products = {
    # Add a width to the shared options for each variant.
    'small': base.extend(width=320),
    'medium': base.extend(width=640),
    'large': base.extend(width=1280),
}
product_urls = client.variants(source=source_url, variants=products)

# Access a URL by its variant name.
print('Small:', product_urls['small'])
print('Medium:', product_urls['medium'])
print('Large:', product_urls['large'])
