from imgproxykit import Client

client = Client(
    'http://localhost:8081',
    key='736563726574',  # (1)!
    salt='73616c74',
)
source_url = 'https://picsum.photos/id/237/1600/1200'

imgproxy_url = client.url(source=source_url)
print(imgproxy_url)
