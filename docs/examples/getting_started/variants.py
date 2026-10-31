from imgproxykit import Client, Transform

client = Client('http://localhost:8080')
source_url = 'https://picsum.photos/id/237/1600/1200'

base = Transform(quality=85, format='webp')  # (1)!
products = {
    'small': base.extend(width=320),  # (2)!
    'medium': base.extend(width=640),
    'large': base.extend(width=1280),
}
product_urls = client.variants(source=source_url, variants=products)

print('Small:', product_urls['small'])
print('Medium:', product_urls['medium'])
print('Large:', product_urls['large'])
