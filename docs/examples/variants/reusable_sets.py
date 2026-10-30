"""
Reuse a set of transformations across source images.

>>> list(dog_urls) == list(pug_urls)
True
>>> dog_urls['small'] != pug_urls['small']
True
>>> [option.name for option in sizes['small'].options]
['quality', 'format', 'width']
"""

from imgproxykit import Client, Transform

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
dog_source = 'https://picsum.photos/id/237/1600/1200'
pug_source = 'https://picsum.photos/id/1025/1600/1200'

# Share quality and output format across all variants.
base = Transform(quality=85, format='webp')
sizes = {
    'small': base.extend(width=320),
    'medium': base.extend(width=640),
    'large': base.extend(width=1280),
}

# Reuse the same set for different source images.
dog_urls = client.variants(source=dog_source, variants=sizes)
pug_urls = client.variants(source=pug_source, variants=sizes)

print(dog_urls['small'])
print(pug_urls['small'])
