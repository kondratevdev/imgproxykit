from imgproxykit import Client, Transform

client = Client('http://localhost:8080', use_short_options=True)  # (1)!
source_url = 'https://picsum.photos/id/237/1600/1200'

image_url = client.url(
    source=source_url,
    transform=Transform(width=300, quality=85),
)
print(image_url)
