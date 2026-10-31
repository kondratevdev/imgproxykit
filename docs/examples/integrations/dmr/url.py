from typing import Final

from dmr import Controller
from dmr.plugins.pydantic import PydanticFastSerializer
from pydantic import BaseModel

from imgproxykit.integrations.django import imgproxy_url

_SOURCE_URL: Final = 'https://originals.example.com/photo.jpg'


class ImageResponse(BaseModel):
    """Generated image URL."""

    image: str


class ImageController(Controller[PydanticFastSerializer]):
    """Serve a transformed image URL."""

    def get(self) -> ImageResponse:
        """Return a transformed image URL."""
        image = imgproxy_url(_SOURCE_URL, 'thumbnail')  # (1)!
        return ImageResponse(image=image)  # (2)!
