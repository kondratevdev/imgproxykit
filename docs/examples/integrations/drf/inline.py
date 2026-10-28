"""
Serialize an image using inline transformations.

>>> from django.test import override_settings
>>> with override_settings(
...     IMGPROXYKIT={
...         'client': {'base_url': 'https://imgproxy.example.com'},
...     }
... ):
...     product = ProductSerializer({
...         'image': 'https://originals.example.com/42.jpg'
...     })
...     images = product.data
>>> images['thumbnail'].startswith('https://imgproxy.example.com/unsafe/')
True
>>> '/width:160/height:160/' in images['thumbnail']
True
>>> list(images['images'])
['small', 'large']
"""

from rest_framework import serializers

from imgproxykit import Transform
from imgproxykit.integrations.drf import ImgproxyURLField, ImgproxyVariantsField


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return a product image at explicitly configured sizes."""

    thumbnail = ImgproxyURLField(
        source='image',
        transform=Transform(width=160, height=160),
    )
    images = ImgproxyVariantsField(
        source='image',
        variants={
            'small': Transform(width=320),
            'large': Transform(width=1280),
        },
    )
