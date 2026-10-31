from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('http://localhost:8080')  # (1)!
source_url = 'https://picsum.photos/id/237/1600/1200'  # (2)!

thumbnail = Transform(
    Resize.fill(width=300, height=300),
    format='webp',
)

thumbnail_url = client.url(source=source_url, transform=thumbnail)  # (3)!
print(thumbnail_url)
