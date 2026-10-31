from imgproxykit import Client

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

image_url = client.url(source=source_url)
print(image_url)
