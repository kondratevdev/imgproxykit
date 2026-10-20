"""
Select JPEG output with a white background.

>>> url.split('/unsafe/')[1].split('/')[:-1]
['background:ffffff', 'format:jpg', 'quality:85', 'strip_metadata:1']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Background

client = Client('https://images.example.com')
jpeg = Transform(
    Background(color='ffffff'),
    format='jpg',
    quality=85,
    strip_metadata=True,
)
url = client.url('https://example.com/logo.png', transform=jpeg)
