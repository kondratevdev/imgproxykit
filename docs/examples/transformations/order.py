"""
Preserve repeated options and append scalar keyword options.

>>> [option.value for option in transform.options]
[80, 90, 85]
>>> url.split('/unsafe/')[1].split('/')[:-1]
['quality:80', 'quality:90', 'quality:85']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Quality

client = Client('https://images.example.com')
transform = Transform(Quality(80), Quality(90), quality=85)
url = client.url('https://example.com/photo.jpg', transform=transform)
