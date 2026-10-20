"""
Use a deployment path prefix and a source URI.

>>> url
'https://images.example.com/imgproxy/unsafe/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
"""

from imgproxykit import Client

client = Client('https://images.example.com/imgproxy/')
source = 'https://example.com/photo.jpg'
url = client.url(source)
