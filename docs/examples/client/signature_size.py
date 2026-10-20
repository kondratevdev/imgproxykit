"""
Match a server configured with a 16-byte signature.

>>> from base64 import urlsafe_b64decode
>>> signature = url.split('/')[3]
>>> len(urlsafe_b64decode(signature + '=='))
16
"""

from imgproxykit import Client

client = Client(
    'https://images.example.com',
    key='736563726574',
    salt='73616c74',
    signature_size=16,
)
url = client.url('https://example.com/photo.jpg')
