"""
Sign a URL with example credentials.

>>> imgproxy_url.startswith('https://imgproxy.example.com/unsafe/')
False
>>> imgproxy_url == client.url(source=source_url)
True
"""

from imgproxykit import Client

client = Client(
    'https://imgproxy.example.com',
    # Replace with your imgproxy server's hex-encoded key and salt.
    key='736563726574',
    salt='73616c74',
)
source_url = 'https://originals.example.com/photo.jpg'

imgproxy_url = client.url(source=source_url)
