"""
Combine a square crop, gravity, and pixel density.

>>> thumbnail_url.split('/unsafe/')[1].split('/')[:-1]
['resize:fill:300:300', 'gravity:ce', 'dpr:2']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Gravity, Resize

# Public URL of your imgproxy server.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

# Combine structured options with a scalar keyword.
thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    Gravity(position='ce'),
    dpr=2,
)

# Build the URL; imgproxy processes the image when the URL is requested.
thumbnail_url = client.url(source=source_url, transform=thumbnail)

print(thumbnail_url)
