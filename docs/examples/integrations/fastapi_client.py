"""
Register a client and use it in a FastAPI route.

>>> import asyncio
>>> from fastapi import Request
>>> async def example():
...     client = await get_imgproxy(Request({'type': 'http', 'app': app}))
...     return await get_product(42, client)
>>> image_url = asyncio.run(example()).image_url
>>> image_url.startswith(
...     'https://imgproxy.example.com/unsafe/width:320/format:webp/'
... )
True
"""

from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()
imgproxykit = Client('https://imgproxy.example.com')

get_imgproxy = add_imgproxy(app, imgproxykit)

# Define a reusable transformation for 320-pixel-wide WebP thumbnails.
thumbnail = Transform(width=320, format='webp')


class ProductResponse(BaseModel):
    """Product image returned by the API."""

    image_url: str


@app.get('/products/{product_id}')
async def get_product(
    product_id: int,
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> ProductResponse:
    """Build a thumbnail URL for a product."""
    source = f'https://originals.example.com/products/{product_id}.jpg'
    thumbnail_url = imgproxy.url(source, transform=thumbnail)
    return ProductResponse(image_url=thumbnail_url)
