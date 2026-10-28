from typing import Any

from rest_framework import serializers

from imgproxykit.integrations.drf import ImgproxyURLField, ImgproxyVariantsField


class ImageSerializer(serializers.Serializer[Any]):
    """Return a preview URL and responsive variants for one source."""

    url = ImgproxyURLField(source='image', transform='preview')
    variants = ImgproxyVariantsField(source='image', variants='responsive')
