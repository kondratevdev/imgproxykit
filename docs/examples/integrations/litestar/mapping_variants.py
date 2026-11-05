from dataclasses import dataclass
from typing import Final

from litestar import Litestar, get
from litestar.di import NamedDependency

from imgproxykit import Client, Transform
from imgproxykit.integrations.litestar import ImgproxyPlugin

_PRODUCT_IMAGE: Final = 'https://media.example.com/products/42.jpg'

_PRODUCT_VARIANTS: Final = {  # (1)!
    'small': Transform(width=320),
    'large': Transform(width=1280),
}


@dataclass(frozen=True, slots=True)
class ProductResponse:
    """Named image variants."""

    images: dict[str, str]


@get('/products/42')
async def get_product(
    imgproxy: NamedDependency[Client],
) -> ProductResponse:
    """Return named image variants."""
    images = imgproxy.variants(
        _PRODUCT_IMAGE,
        variants=_PRODUCT_VARIANTS,
    )  # (2)!
    return ProductResponse(images=images)


app = Litestar(
    route_handlers=[get_product],
    plugins=[ImgproxyPlugin(Client('https://imgproxy.example.com'))],
)
