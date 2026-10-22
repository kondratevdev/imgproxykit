"""
Combine a square crop, gravity, and pixel density.

>>> thumbnail_url.split('/unsafe/')[1].split('/')[:-1]
['resize:fill:300:300', 'gravity:ce', 'dpr:2']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Gravity, Resize

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'

thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    Gravity(position='ce'),
    dpr=2,
)
thumbnail_url = client.url(source=source_url, transform=thumbnail)
