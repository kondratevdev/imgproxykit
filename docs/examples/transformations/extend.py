from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

base = Transform(quality=85, format='webp')  # (1)!

thumbnail = base.extend(Resize.fill(width=300, height=300))  # (2)!

retina = thumbnail.extend(dpr=2)  # (3)!

print('Base:', client.url(source_url, transform=base))
print('Thumbnail:', client.url(source_url, transform=thumbnail))
print('Retina:', client.url(source_url, transform=retina))
