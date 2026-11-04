from typing import Annotated, Final

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

_PRODUCT_IMAGE: Final = 'https://media.example.com/products/42.jpg'

app = FastAPI()
get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))

_PRODUCT_VARIANTS: Final = {  # (1)!
    'small': Transform(width=320),
    'large': Transform(width=1280),
}


class ProductResponse(BaseModel):
    """Named image variants."""

    images: dict[str, str]


@app.get('/products/42')
async def get_product(
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> ProductResponse:
    """Return named image variants."""
    images = imgproxy.variants(_PRODUCT_IMAGE, variants=_PRODUCT_VARIANTS)  # (2)!
    return ProductResponse(images=images)
