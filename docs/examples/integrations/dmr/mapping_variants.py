from typing import Final

from dmr import Controller
from dmr.plugins.pydantic import PydanticFastSerializer
from pydantic import BaseModel

from imgproxykit import Transform
from imgproxykit.integrations.django import imgproxy_variants

_SOURCE_URL: Final = 'https://originals.example.com/photo.jpg'


class ProductImages(BaseModel):
    """Named image variants exposed by the API."""

    small: str
    large: str


class ImageResponse(BaseModel):
    """Named image variants."""

    images: ProductImages  # (1)!


class ImageController(Controller[PydanticFastSerializer]):
    """Serve named image variants."""

    def get(self) -> ImageResponse:
        """Return the configured image variants."""
        images = imgproxy_variants(
            _SOURCE_URL,
            {  # (2)!
                'small': Transform(width=320),
                'large': Transform(width=1280),
            },
        )
        return ImageResponse(images=ProductImages(**images))  # (3)!
