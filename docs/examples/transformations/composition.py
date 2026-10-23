"""
Compose transformations from reusable groups of options.

>>> [option.name for option in thumbnail.options]
['quality', 'format', 'resize']
>>> [option.name for option in retina.options]
['quality', 'format', 'resize', 'dpr']
>>> [option.name for option in base.options]
['quality', 'format']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Define reusable groups of processing options.
base = Transform(quality=85, format='webp')
square = Transform(Resize(width=300, height=300, mode='fill'))

# Combine options from both transformations.
thumbnail = Transform(*base.options, *square.options)

# Add a higher pixel density to the combined options.
retina = Transform(*thumbnail.options, dpr=2)

# Build URLs using the composed transformations.
thumbnail_url = client.url(source=source_url, transform=thumbnail)
retina_url = client.url(source=source_url, transform=retina)

print(thumbnail_url)
print(retina_url)
