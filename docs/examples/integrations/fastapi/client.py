from typing import Annotated, Final

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

_PRODUCT_IMAGE: Final = 'https://media.example.com/products/42.jpg'

app = FastAPI()
get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))


class ProductResponse(BaseModel):
    """Product image URL."""

    thumbnail: str


@app.get('/products/42')
async def get_product(
    imgproxy: Annotated[Client, Depends(get_imgproxy)],  # (1)!
) -> ProductResponse:
    """Return a transformed image URL."""
    thumbnail = imgproxy.url(_PRODUCT_IMAGE, transform=Transform(width=160))
    return ProductResponse(thumbnail=thumbnail)
