from rest_framework import serializers

from imgproxykit import Transform
from imgproxykit.integrations.drf import ImgproxyVariantsField


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return a product image at explicitly configured sizes."""

    images = ImgproxyVariantsField(
        source='image',
        variants={  # (1)!
            'small': Transform(width=320),
            'large': Transform(width=1280),
        },
    )
