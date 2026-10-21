"""
Build an unsigned URL.

>>> url
'https://imgproxykit.url.com/unsafe/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
"""

from imgproxykit import Client

client = Client('https://imgproxykit.url.com')
image = 'https://example.com/photo.jpg'

url = client.url(image)
