"""
Combine server preset references with processing options.

>>> thumbnail_url.split('/unsafe/')[1].split('/')[:-1]
['preset:thumbnail:watermarked', 'quality:85', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Preset

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'

thumbnail = Transform(
    Preset('thumbnail', 'watermarked'),
    quality=85,
    format='webp',
)
thumbnail_url = client.url(source=source_url, transform=thumbnail)
