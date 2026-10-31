from typing import Annotated, Final

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

_SOURCE_URL: Final = 'https://originals.example.com/photo.jpg'
_THUMBNAIL: Final = Transform(width=300, format='webp')

app = FastAPI()
get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))  # (1)!


class ImageResponse(BaseModel):
    """Generated image URL."""

    image: str


@app.get('/image')
async def get_image(
    imgproxy: Annotated[Client, Depends(get_imgproxy)],  # (2)!
) -> ImageResponse:
    """Return a transformed image URL."""
    image = imgproxy.url(_SOURCE_URL, transform=_THUMBNAIL)
    return ImageResponse(image=image)
