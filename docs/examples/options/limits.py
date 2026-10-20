"""
Set per-request source limits.

>>> url.split('/unsafe/')[1].split('/')[:-1]
['max_src_resolution:20', 'max_src_file_size:5000000']
"""

from imgproxykit import Client, Transform

client = Client('https://images.example.com')
limited = Transform(
    max_src_resolution=20,
    max_src_file_size=5_000_000,
)
url = client.url('https://example.com/photo.jpg', transform=limited)
