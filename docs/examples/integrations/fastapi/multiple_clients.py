"""
Register signed and unsigned clients and inject both into a FastAPI route.

>>> import asyncio
>>> from fastapi import Request
>>> async def example():
...     request = Request({'type': 'http', 'app': app})
...     signed = await get_signed_imgproxy(request)
...     unsigned = await get_unsigned_imgproxy(request)
...     return await get_product_images(42, signed, unsigned)
>>> images = asyncio.run(example())
>>> images.signed.startswith('https://imgproxy.example.com/')
True
>>> '/unsafe/' not in images.signed
True
>>> images.unsigned.startswith('https://imgproxy.example.com/unsafe/')
True
"""

from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()

# Register the signed client under the default name.
get_signed_imgproxy = add_imgproxy(
    app,
    Client(
        'https://imgproxy.example.com',
        # Replace the example key and salt with your imgproxy credentials.
        key='736563726574',
        salt='73616c74',
    ),
)
# Give the unsigned client its own name to keep both registrations.
get_unsigned_imgproxy = add_imgproxy(
    app,
    Client('https://imgproxy.example.com'),
    name='unsigned_imgproxy',
)


class ProductImageUrls(BaseModel):
    """Signed and unsigned URLs for a product image."""

    signed: str
    unsigned: str


@app.get('/products/{product_id}/images')
async def get_product_images(
    product_id: int,
    signed: Annotated[Client, Depends(get_signed_imgproxy)],
    unsigned: Annotated[Client, Depends(get_unsigned_imgproxy)],
) -> ProductImageUrls:
    """Build image URLs with each client's signing configuration."""
    source = f'https://originals.example.com/products/{product_id}.jpg'
    # Each dependency supplies a client with its own signing settings.
    return ProductImageUrls(
        signed=signed.url(source),
        unsigned=unsigned.url(source),
    )
