"""
Sign a URL with example credentials.

>>> imgproxy_url.startswith('http://localhost:8081/unsafe/')
False
>>> imgproxy_url == client.url(source=source_url)
True
"""

from imgproxykit import Client

client = Client(
    'http://localhost:8081',
    # Replace with your imgproxy server's hex-encoded key and salt.
    key='736563726574',
    salt='73616c74',
)
source_url = 'https://picsum.photos/id/237/1600/1200'

imgproxy_url = client.url(source=source_url)

print(imgproxy_url)
