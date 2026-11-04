from dataclasses import dataclass
from typing import Annotated, Final

from dmr import Controller
from dmr.plugins.pydantic import PydanticFastSerializer
from pydantic import BaseModel

from imgproxykit import Transform
from imgproxykit.integrations.django import imgproxy_variants

_SOURCE_URL: Final = 'https://originals.example.com/photo.jpg'


@dataclass(frozen=True, slots=True)
class ProductImages:
    """Named image variants exposed by the API."""

    small: Annotated[str, Transform(width=320)]  # (1)!
    large: Annotated[str, Transform(width=1280)]


class ImageResponse(BaseModel):
    """Named image variants."""

    images: ProductImages  # (2)!


class ImageController(Controller[PydanticFastSerializer]):
    """Serve named image variants."""

    def get(self) -> ImageResponse:
        """Return the configured image variants."""
        images = imgproxy_variants(_SOURCE_URL, ProductImages)  # (3)!
        return ImageResponse(images=images)
