"""
Combine server preset references with processing options.

>>> thumbnail_url.split('/unsafe/')[1].split('/')[:-1]
['preset:thumbnail:small', 'quality:85', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Preset

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Combine server presets with explicit processing options.
thumbnail = Transform(
    Preset('thumbnail', 'small'),
    quality=85,
    format='webp',
)

# Build the URL; imgproxy processes the image when the URL is requested.
thumbnail_url = client.url(source=source_url, transform=thumbnail)

print(thumbnail_url)
