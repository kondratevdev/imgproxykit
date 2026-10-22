"""
Create a small blurred preview.

>>> preview_url.split('/unsafe/')[1].split('/')[:-1]
['resize:fit:32:32', 'blur:2', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'

preview = Transform(
    Resize(width=32, height=32, mode='fit'),
    blur=2,
    format='webp',
)
preview_url = client.url(source=source_url, transform=preview)
