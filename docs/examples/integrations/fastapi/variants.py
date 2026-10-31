from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()

get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))

base = Transform(format='webp')


@dataclass(frozen=True, slots=True)
class ProductImages:
    """Declare the image response fields and their transformations."""

    thumbnail: Annotated[str, base.extend(width=320)]  # (1)!
    preview: Annotated[str, base.extend(width=1280)]


class ProductResponse(BaseModel):
    """Product and its image variants returned by the API."""

    id: int
    images: ProductImages  # (2)!


@app.get('/products/{product_id}')
async def get_product(
    product_id: int,
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> ProductResponse:
    """Return a product with image variants."""
    source = f'https://originals.example.com/products/{product_id}.jpg'
    images = imgproxy.variants(source, variants=ProductImages)  # (3)!
    return ProductResponse(id=product_id, images=images)
