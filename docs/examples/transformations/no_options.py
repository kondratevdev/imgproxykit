"""
Leave processing options to the server.

>>> default_url == none_url == empty_url
True
>>> default_url
'https://imgproxy.example.com/unsafe/aHR0cHM6Ly9vcmlnaW5hbHMuZXhhbXBsZS5jb20vcGhvdG8uanBn'
"""

from imgproxykit import Client, Transform

client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'

default_url = client.url(source=source_url)
none_url = client.url(source=source_url, transform=None)
empty_url = client.url(source=source_url, transform=Transform())
