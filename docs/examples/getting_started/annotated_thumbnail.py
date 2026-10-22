"""
Build a thumbnail URL with annotations for the documentation home page.

>>> thumbnail_url.split('/unsafe/')[1].split('/')[0:2]
['resize:fill:300:300', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://imgproxy.example.com')  # (1)!
# Original image accessible to your imgproxy server.
source_url = 'https://originals.example.com/photo.jpg'

thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),  # Resize and crop to a square.
    format='webp',  # Select the output format with a scalar keyword.
)

# Build the URL; imgproxy processes the image when the URL is requested.
thumbnail_url = client.url(source=source_url, transform=thumbnail)
