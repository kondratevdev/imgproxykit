from dataclasses import dataclass
from typing import Annotated

from rest_framework import serializers

from imgproxykit import Transform
from imgproxykit.integrations.drf import ImgproxyVariantsField


@dataclass(frozen=True, slots=True)
class ProductImages:
    """Declare reusable image variants."""

    small: Annotated[str, Transform(width=320)]  # (1)!
    large: Annotated[str, Transform(width=1280)]


class ProductSerializer(serializers.Serializer[dict[str, str]]):
    """Return image variants as a dictionary of URLs."""

    images = ImgproxyVariantsField(
        source='image',
        variants=ProductImages,  # (2)!
    )
