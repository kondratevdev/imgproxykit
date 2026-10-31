from imgproxykit import Client, Transform
from imgproxykit.options import Gravity, Resize

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

thumbnail = Transform(
    Resize.fill(width=300, height=300),  # (1)!
    Gravity.center(),  # (2)!
    dpr=2,  # (3)!
)

thumbnail_url = client.url(source=source_url, transform=thumbnail)

print(thumbnail_url)
