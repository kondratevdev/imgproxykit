"""
Reuse processing options for different source images.

>>> len(thumbnail_urls)
2
>>> thumbnail_urls[0] != thumbnail_urls[1]
True
>>> all(
...     '/resize:fill:300:300/format:webp/' in thumbnail_url
...     for thumbnail_url in thumbnail_urls
... )
True
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://imgproxy.example.com')
# Reuse the same transformation for multiple source images.
thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    format='webp',
)

source_urls = [
    'https://originals.example.com/sneakers.jpg',
    'https://originals.example.com/backpack.jpg',
]
thumbnail_urls = [
    client.url(source=source_url, transform=thumbnail)
    for source_url in source_urls
]
