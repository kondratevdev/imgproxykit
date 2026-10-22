"""
Match a server configured with a comma as its arguments separator.

>>> imgproxy_url
'https://imgproxy.example.com/unsafe/resize,fill,300,200/format,webp/aHR0cHM6Ly9vcmlnaW5hbHMuZXhhbXBsZS5jb20vcGhvdG8uanBn'
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client(
    'https://imgproxy.example.com',
    arguments_separator=',',
)
source_url = 'https://originals.example.com/photo.jpg'

imgproxy_url = client.url(
    source=source_url,
    transform=Transform(
        Resize(mode='fill', width=300, height=200),
        format='webp',
    ),
)
