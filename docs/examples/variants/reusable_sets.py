from pprint import pprint

from imgproxykit import Client, Transform

client = Client('http://localhost:8080')
dog_source = 'https://picsum.photos/id/237/1600/1200'
pug_source = 'https://picsum.photos/id/1025/1600/1200'

base = Transform(quality=85, format='webp')  # (1)!
sizes = {
    'small': base.extend(width=320),
    'medium': base.extend(width=640),
    'large': base.extend(width=1280),
}

dog_urls = client.variants(source=dog_source, variants=sizes)  # (2)!
pug_urls = client.variants(source=pug_source, variants=sizes)

pprint({'Dog': dog_urls}, sort_dicts=False)
pprint({'Pug': pug_urls}, sort_dicts=False)
