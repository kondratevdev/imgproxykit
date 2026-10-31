from dataclasses import dataclass
from typing import Annotated, Final

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

_SOURCE_URL: Final = 'https://originals.example.com/photo.jpg'
_BASE: Final = Transform(format='webp')

app = FastAPI()
get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))


@dataclass(frozen=True, slots=True)
class ProductImages:
    """Declare the image response fields and their transformations."""

    thumbnail: Annotated[str, _BASE.extend(width=320)]  # (1)!
    preview: Annotated[str, _BASE.extend(width=1280)]


class ImageResponse(BaseModel):
    """Named image variants."""

    images: ProductImages  # (2)!


@app.get('/image')
async def get_image(
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> ImageResponse:
    """Return named image variants."""
    images = imgproxy.variants(_SOURCE_URL, variants=ProductImages)  # (3)!
    return ImageResponse(images=images)
