"""
Build an unsigned URL.

>>> imgproxy_url
'https://imgproxy.example.com/unsafe/aHR0cHM6Ly9vcmlnaW5hbHMuZXhhbXBsZS5jb20vcGhvdG8uanBn'
"""

from imgproxykit import Client

# Public URL of your imgproxy server.
client = Client('https://imgproxy.example.com')
source_url = 'https://originals.example.com/photo.jpg'

imgproxy_url = client.url(source=source_url)
