"""
Use scalar option instances and keyword arguments together.

>>> [option.name for option in optimized.options]
['quality', 'format']
>>> '/quality:85/format:webp/' in image_url
True
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Quality

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Pass a scalar option instance or use its keyword form.
optimized = Transform(
    Quality(85),  # Equivalent to quality=85.
    format='webp',  # Equivalent to Format('webp').
)

# Build the URL; imgproxy processes the image when the URL is requested.
image_url = client.url(source=source_url, transform=optimized)

print(image_url)
