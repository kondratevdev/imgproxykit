"""
Reuse processing options for different images.

>>> len(thumbnails)
2
>>> thumbnails[0] != thumbnails[1]
True
>>> all('/resize:fill:300:300/format:webp/' in url for url in thumbnails)
True
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://images.example.com')
thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    format='webp',
)

images = [
    'https://example.com/sneakers.jpg',
    'https://example.com/backpack.jpg',
]
thumbnails = [client.url(image, transform=thumbnail) for image in images]
