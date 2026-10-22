"""
Match a server configured with a 16-byte signature.

>>> from base64 import urlsafe_b64decode
>>> signature = imgproxy_url.split('/')[3]
>>> len(urlsafe_b64decode(signature + '=='))
16
"""

from imgproxykit import Client

client = Client(
    'https://imgproxy.example.com',
    key='736563726574',
    salt='73616c74',
    signature_size=16,
)
source_url = 'https://originals.example.com/photo.jpg'

imgproxy_url = client.url(source=source_url)
