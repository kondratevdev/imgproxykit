"""
Sign a URL with example credentials.

>>> url.startswith('https://images.example.com/unsafe/')
False
>>> url == client.url(source)
True
"""

from imgproxykit import Client

client = Client(
    'https://images.example.com',
    key='736563726574',
    salt='73616c74',
)
source = 'https://example.com/photo.jpg'

url = client.url(source)
