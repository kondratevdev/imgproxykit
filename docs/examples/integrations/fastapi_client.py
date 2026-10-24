"""
Register a client and use it in a FastAPI route.

>>> import asyncio
>>> from fastapi import Request
>>> async def example():
...     client = await get_imgproxy(Request({'type': 'http', 'app': app}))
...     return await get_product(42, client)
>>> product = asyncio.run(example())
>>> product.id
42
>>> product.images.thumbnail.startswith(
...     'https://imgproxy.example.com/unsafe/width:320/format:webp/'
... )
True
>>> product.images.preview.startswith(
...     'https://imgproxy.example.com/unsafe/width:1280/format:webp/'
... )
True
"""

from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()
# Define and register client:
imgproxy = Client('https://imgproxy.example.com')
get_imgproxy = add_imgproxy(app, imgproxy)

# Define reusable image variants for product cards and previews:
product_variants = {
    'thumbnail': Transform(width=320, format='webp'),
    'preview': Transform(width=1280, format='webp'),
}


class ProductImages(BaseModel):
    """Image variants returned for a product."""

    thumbnail: str
    preview: str


class ProductResponse(BaseModel):
    """Product and its image variants returned by the API."""

    id: int
    images: ProductImages


@app.get('/products/{product_id}')
async def get_product(
    product_id: int,
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> ProductResponse:
    """Return a product with image variants."""
    source = f'https://originals.example.com/products/{product_id}.jpg'
    images = imgproxy.variants(source, variants=product_variants)
    return ProductResponse(
        id=product_id,
        images=ProductImages(**images),
    )
