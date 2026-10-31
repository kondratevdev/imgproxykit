from rest_framework import serializers

from imgproxykit import Transform
from imgproxykit.integrations.drf import (
    ImgproxyURLField,
    ImgproxyVariantsField,
)


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return a product image at explicitly configured sizes."""

    thumbnail = ImgproxyURLField(
        source='image',
        transform=Transform(width=160, height=160),  # (1)!
    )
    images = ImgproxyVariantsField(
        source='image',
        variants={  # (2)!
            'small': Transform(width=320),
            'large': Transform(width=1280),
        },
    )
