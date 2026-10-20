"""
Leave processing options to the server.

>>> default_url == none_url == empty_url
True
>>> default_url
'https://images.example.com/unsafe/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
"""

from imgproxykit import Client, Transform

client = Client('https://images.example.com')
source = 'https://example.com/photo.jpg'

default_url = client.url(source)
none_url = client.url(source, transform=None)
empty_url = client.url(source, transform=Transform())
