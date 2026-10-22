"""
Set per-request source limits.

>>> imgproxy_url.split('/unsafe/')[1].split('/')[:-1]
['max_src_resolution:20', 'max_src_file_size:5000000']
"""

from imgproxykit import Client, Transform

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'

limited = Transform(
    max_src_resolution=20,
    max_src_file_size=5_000_000,
)
imgproxy_url = client.url(source=source_url, transform=limited)
