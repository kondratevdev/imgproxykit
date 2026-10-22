"""
Use a deployment path prefix and a source URI.

>>> imgproxy_url
'https://imgproxy.example.com/imgproxy/unsafe/aHR0cHM6Ly9vcmlnaW5hbHMuZXhhbXBsZS5jb20vcGhvdG8uanBn'
"""

from imgproxykit import Client

# Include the path prefix where your imgproxy server is exposed.
client = Client('https://imgproxy.example.com/imgproxy/')

source_url = 'https://originals.example.com/photo.jpg'
imgproxy_url = client.url(source=source_url)
