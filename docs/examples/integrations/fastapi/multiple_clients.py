from typing import Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy

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


class ProductImageUrls(BaseModel):
    """Signed and unsigned URLs for a product image."""

    signed: str
    unsigned: str


@app.get('/products/{product_id}/images')
async def get_product_images(
    product_id: int,
    signed: Annotated[Client, Depends(get_signed_imgproxy)],  # (3)!
    unsigned: Annotated[Client, Depends(get_unsigned_imgproxy)],
) -> ProductImageUrls:
    """Build image URLs with each client's signing configuration."""
    source = f'https://originals.example.com/products/{product_id}.jpg'
    return ProductImageUrls(
        signed=signed.url(source),
        unsigned=unsigned.url(source),
    )
