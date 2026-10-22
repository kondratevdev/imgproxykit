"""
Select JPEG output with a white background.

>>> jpeg_url.split('/unsafe/')[1].split('/')[:-1]
['background:ffffff', 'format:jpg', 'quality:85', 'strip_metadata:1']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Background

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/logo.png'

jpeg = Transform(
    Background(color='ffffff'),
    format='jpg',
    quality=85,
    strip_metadata=True,
)
jpeg_url = client.url(source=source_url, transform=jpeg)
