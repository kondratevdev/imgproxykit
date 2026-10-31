from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()
get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))  # (1)!


class ProductResponse(BaseModel):
    """Product and its image URL returned by the API."""

    id: int
    image: str


@app.get('/products/{product_id}')
async def get_product(
    product_id: int,
    imgproxy: Annotated[Client, Depends(get_imgproxy)],  # (2)!
) -> ProductResponse:
    """Return a product with a transformed image URL."""
    source = f'https://originals.example.com/products/{product_id}.jpg'
    image = imgproxy.url(source, transform=Transform(width=300, format='webp'))
    return ProductResponse(id=product_id, image=image)
