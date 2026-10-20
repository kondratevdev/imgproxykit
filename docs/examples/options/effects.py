"""
Create a small blurred preview.

>>> url.split('/unsafe/')[1].split('/')[:-1]
['resize:fit:32:32', 'blur:2', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://images.example.com')
preview = Transform(
    Resize(width=32, height=32, mode='fit'),
    blur=2,
    format='webp',
)
url = client.url('https://example.com/photo.jpg', transform=preview)
