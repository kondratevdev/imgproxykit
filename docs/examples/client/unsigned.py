"""
Customize the unsigned URL marker.

>>> url.split('/')[3]
'public'
"""

from imgproxykit import Client

client = Client(
    'https://images.example.com',
    unsigned_signature='public',
)
url = client.url('https://example.com/photo.jpg')
