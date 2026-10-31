from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

default = Transform(Resize.fit(width=300))  # (1)!
no_enlarge = Transform(Resize.fit(width=300, enlarge=False))  # (2)!

default_url = client.url(source=source_url, transform=default)
no_enlarge_url = client.url(source=source_url, transform=no_enlarge)

print('Omitted:', default_url)
print('Explicit False:', no_enlarge_url)
