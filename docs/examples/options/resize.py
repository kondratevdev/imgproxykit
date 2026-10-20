"""
Combine a square crop, gravity, and pixel density.

>>> url.split('/unsafe/')[1].split('/')[:-1]
['resize:fill:300:300', 'gravity:ce', 'dpr:2']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Gravity, Resize

client = Client('https://images.example.com')
thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    Gravity(position='ce'),
    dpr=2,
)
url = client.url('https://example.com/photo.jpg', transform=thumbnail)
