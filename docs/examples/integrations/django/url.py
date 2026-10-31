from django.conf import settings
from django.test import override_settings

from docs.examples.integrations.django.settings import IMGPROXYKIT

if not settings.configured:
    settings.configure()

with override_settings(IMGPROXYKIT=IMGPROXYKIT):
    from imgproxykit.integrations.django import imgproxy_url

    source = 'https://media.example.com/products/42.jpg'
    image_url = imgproxy_url(source, 'thumbnail')  # (1)!
    print(image_url)
