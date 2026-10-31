from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('http://localhost:8080')
thumbnail = Transform(  # (1)!
    Resize.fill(width=300, height=300),
    format='webp',
)

source_urls = [
    'https://picsum.photos/id/237/1600/1200',
    'https://picsum.photos/id/1025/1600/1200',
]
thumbnail_urls = [
    client.url(source=source_url, transform=thumbnail)
    for source_url in source_urls
]

print(*thumbnail_urls, sep='\n')
