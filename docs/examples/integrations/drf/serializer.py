"""
Serialize an image using named transformations from Django settings.

>>> from django.test import override_settings
>>> from docs.examples.integrations.django.settings import IMGPROXYKIT
>>> with override_settings(IMGPROXYKIT=IMGPROXYKIT):
...     product = ProductSerializer({
...         'image': 'https://originals.example.com/42.jpg'
...     })
...     images = product.data
>>> '/width:300/height:300/format:webp/' in images['thumbnail']
True
>>> list(images['images'])
['small', 'large']
>>> '/width:1280/format:webp/' in images['images']['large']
True
"""

from rest_framework import serializers

from imgproxykit.integrations.drf import ImgproxyURLField, ImgproxyVariantsField


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return a thumbnail and named variants for a product image."""

    thumbnail = ImgproxyURLField(source='image', transform='thumbnail')
    images = ImgproxyVariantsField(source='image', variants='product')
