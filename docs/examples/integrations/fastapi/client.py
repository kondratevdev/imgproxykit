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
...     'https://imgproxy.example.com/unsafe/format:webp/width:320/'
... )
True
>>> product.images.preview.startswith(
...     'https://imgproxy.example.com/unsafe/format:webp/width:1280/'
... )
True
"""

from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()

# Keep the returned dependency for use with Depends in route handlers.
get_imgproxy = add_imgproxy(
    app,
    Client('https://imgproxy.example.com'),  # Public imgproxy address.
)

# Reuse these image sizes and output format across products.
base = Transform(format='webp')


@dataclass(frozen=True, slots=True)
class ProductImages:
    """Declare the image response fields and their transformations."""

    thumbnail: Annotated[str, base.extend(width=320)]
    preview: Annotated[str, base.extend(width=1280)]


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
    # Build one URL per variant for the same source image.
    images = imgproxy.variants(source, variants=ProductImages)
    return ProductResponse(id=product_id, images=images)
