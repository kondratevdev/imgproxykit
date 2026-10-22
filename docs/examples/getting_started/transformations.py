"""
Resize an image and select its output format.

>>> thumbnail_url.split('/unsafe/')[1].split('/')[0:2]
['resize:fill:300:300', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

# Public URL of your imgproxy server.
client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'
thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    format='webp',
)

thumbnail_url = client.url(source=source_url, transform=thumbnail)
