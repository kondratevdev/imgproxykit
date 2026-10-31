from imgproxykit import Client, Transform

client = Client('http://localhost:8080', source_encoding='plain')  # (1)!
source_url = 'https://picsum.photos/id/237/1600/1200'  # (2)!

image_url = client.url(
    source=source_url,
    transform=Transform(width=300, format='webp'),
)
print(image_url)
