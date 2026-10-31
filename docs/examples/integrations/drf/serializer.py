from rest_framework import serializers

from imgproxykit.integrations.drf import (
    ImgproxyURLField,
    ImgproxyVariantsField,
)


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return a thumbnail and named variants for a product image."""

    thumbnail = ImgproxyURLField(  # (1)!
        source='image',
        transform='thumbnail',
    )
    images = ImgproxyVariantsField(  # (2)!
        source='image',
        variants='product',
    )
