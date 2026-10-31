from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://imgproxy.example.com')  # (1)!
source_url = 'https://originals.example.com/photo.jpg'  # (2)!

thumbnail = Transform(
    Resize.fill(width=300, height=300),
    format='webp',
)

thumbnail_url = client.url(source=source_url, transform=thumbnail)  # (3)!
print(thumbnail_url)
