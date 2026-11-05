from dataclasses import dataclass
from typing import Final

from litestar import Litestar, get
from litestar.di import NamedDependency

from imgproxykit import Client, Transform
from imgproxykit.integrations.litestar import ImgproxyPlugin

_PRODUCT_IMAGE: Final = 'https://media.example.com/products/42.jpg'


@dataclass(frozen=True, slots=True)
class ProductResponse:
    """Product image URL."""

    thumbnail: str


@get('/products/42')
async def get_product(
    imgproxy: NamedDependency[Client],  # (1)!
) -> ProductResponse:
    """Return a transformed image URL."""
    thumbnail = imgproxy.url(_PRODUCT_IMAGE, transform=Transform(width=160))
    return ProductResponse(thumbnail=thumbnail)


app = Litestar(
    route_handlers=[get_product],
    plugins=[ImgproxyPlugin(Client('https://imgproxy.example.com'))],
)
