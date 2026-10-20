"""
Build an unsigned URL.

>>> url
'https://images.example.com/unsafe/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
"""

from imgproxykit import Client

client = Client('https://images.example.com')
source = 'https://example.com/photo.jpg'

url = client.url(source)
