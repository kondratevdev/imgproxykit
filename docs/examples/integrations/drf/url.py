from rest_framework import serializers

from imgproxykit.integrations.drf import ImgproxyURLField


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return a thumbnail for a product image."""

    thumbnail = ImgproxyURLField(
        source='image',
        transform='thumbnail',  # (1)!
    )
