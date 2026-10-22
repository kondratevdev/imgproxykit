"""
Customize the unsigned URL marker.

>>> imgproxy_url.split('/')[3]
'public'
"""

from imgproxykit import Client

client = Client(
    'https://imgproxy.example.com',
    unsigned_signature='public',
)
source_url = 'https://originals.example.com/photo.jpg'

imgproxy_url = client.url(source=source_url)
