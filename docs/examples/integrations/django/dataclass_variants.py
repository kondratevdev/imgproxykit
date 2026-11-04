from django.conf import settings
from django.test import override_settings

from docs.examples.integrations.django.settings import IMGPROXYKIT

if not settings.configured:
    settings.configure()

with override_settings(IMGPROXYKIT=IMGPROXYKIT):
    from dataclasses import dataclass
    from pprint import pprint
    from typing import Annotated

    from imgproxykit import Transform
    from imgproxykit.integrations.django import imgproxy_variants

    @dataclass(frozen=True, slots=True)
    class ProductImages:
        """Declare named image URLs and their transformations."""

        small: Annotated[str, Transform(width=320)]  # (1)!
        large: Annotated[str, Transform(width=1280)]

    source = 'https://media.example.com/products/42.jpg'
    images = imgproxy_variants(source, ProductImages)  # (2)!

    pprint(images)
