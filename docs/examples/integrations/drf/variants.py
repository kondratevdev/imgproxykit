from rest_framework import serializers

from imgproxykit.integrations.drf import ImgproxyVariantsField


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return named variants for a product image."""

    images = ImgproxyVariantsField(
        source='image',
        variants='product',  # (1)!
    )
