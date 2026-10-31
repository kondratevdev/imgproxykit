from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

base = Transform(quality=85, format='webp')
square = Transform(Resize.fill(width=300, height=300))

thumbnail = base.extend(*square.options)  # (1)!

print(client.url(source_url, transform=thumbnail))
