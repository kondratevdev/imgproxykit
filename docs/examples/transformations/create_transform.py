"""
Define processing options and build an image URL.

>>> [option.name for option in thumbnail.options]
['resize', 'quality', 'format']
>>> '/resize:fill:300:300/quality:85/format:webp/' in thumbnail_url
True
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Define the thumbnail dimensions, quality, and output format.
thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),  # Pass typed option objects.
    quality=85,  # Or scalar keywords, equivalent to Quality(85).
    format='webp',
)

# Build the URL; imgproxy processes the image when the URL is requested.
thumbnail_url = client.url(source=source_url, transform=thumbnail)

print(thumbnail_url)
