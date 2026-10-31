from imgproxykit import Client, Transform
from imgproxykit.options import Format, Quality

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

optimized = Transform(
    Quality(85),  # (1)!
    Format('webp'),
)
keyword_optimized = Transform(quality=85, format='webp')  # (2)!

image_url = client.url(source=source_url, transform=optimized)
keyword_url = client.url(source=source_url, transform=keyword_optimized)

print('Option instance:', image_url)
print('Keyword:', keyword_url)
