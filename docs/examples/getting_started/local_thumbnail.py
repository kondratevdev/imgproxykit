"""
Resize an image and select its output format.

>>> thumbnail_url.split('/unsafe/')[1].split('/')[0:2]
['resize:fill:300:300', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

# Address of the test imgproxy container.
client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

thumbnail = Transform(
    Resize.fill(width=300, height=300),
    format='webp',
)

# Build the URL; imgproxy processes the image when the URL is requested.
thumbnail_url = client.url(source=source_url, transform=thumbnail)
print(thumbnail_url)
