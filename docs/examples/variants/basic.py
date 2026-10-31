from pprint import pprint

from imgproxykit import Client, Transform

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

products = {  # (1)!
    'small': Transform(width=320),
    'medium': Transform(width=640),
    'large': Transform(width=1280),
}

product_urls = client.variants(source=source_url, variants=products)  # (2)!

pprint(product_urls, sort_dicts=False)
