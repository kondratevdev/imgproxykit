from typing import Annotated, Final

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy

_SOURCE_URL: Final = 'https://originals.example.com/photo.jpg'

app = FastAPI()
get_signed_imgproxy = add_imgproxy(  # (1)!
    app,
    Client(
        'https://imgproxy.example.com',
        key='736563726574',
        salt='73616c74',
    ),
)
get_unsigned_imgproxy = add_imgproxy(
    app,
    Client('https://imgproxy.example.com'),
    name='unsigned_imgproxy',  # (2)!
)


class ImageUrls(BaseModel):
    """Signed and unsigned image URLs."""

    signed: str
    unsigned: str


@app.get('/images')
async def get_images(
    signed: Annotated[Client, Depends(get_signed_imgproxy)],  # (3)!
    unsigned: Annotated[Client, Depends(get_unsigned_imgproxy)],
) -> ImageUrls:
    """Build image URLs with each client's signing configuration."""
    return ImageUrls(
        signed=signed.url(_SOURCE_URL),
        unsigned=unsigned.url(_SOURCE_URL),
    )
