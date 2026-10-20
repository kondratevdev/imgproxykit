"""
Combine server preset references with processing options.

>>> url.split('/unsafe/')[1].split('/')[:-1]
['preset:thumbnail:watermarked', 'quality:85', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Preset

client = Client('https://images.example.com')
thumbnail = Transform(
    Preset(names=('thumbnail', 'watermarked')),
    quality=85,
    format='webp',
)
url = client.url('https://example.com/photo.jpg', transform=thumbnail)
