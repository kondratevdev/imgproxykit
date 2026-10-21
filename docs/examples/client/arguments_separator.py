"""
Match a server configured with a comma as its arguments separator.

>>> url
'https://images.example.com/unsafe/resize,fill,300,200/format,webp/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client(
    'https://images.example.com',
    arguments_separator=',',
)
url = client.url(
    'https://example.com/photo.jpg',
    transform=Transform(
        Resize(mode='fill', width=300, height=200),
        format='webp',
    ),
)
