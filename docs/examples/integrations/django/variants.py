from django.conf import settings
from django.test import override_settings

from docs.examples.integrations.django.settings import IMGPROXYKIT

if not settings.configured:
    settings.configure()

with override_settings(IMGPROXYKIT=IMGPROXYKIT):
    from pprint import pprint

    from imgproxykit.integrations.django import imgproxy_variants

    source = 'https://media.example.com/products/42.jpg'
    images = imgproxy_variants(source, 'product')  # (1)!
    pprint(images, sort_dicts=False)
