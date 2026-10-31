from dmr import Controller, Path
from dmr.plugins.pydantic import PydanticFastSerializer
from pydantic import BaseModel

from imgproxykit.integrations.django import imgproxy_url


class ProductPath(BaseModel):
    """Identify the product requested by the URL."""

    product_id: int


class ProductResponse(BaseModel):
    """Product and its generated image URL."""

    id: int
    image: str


class ProductController(Controller[PydanticFastSerializer]):
    """Serve a product with its image URL."""

    def get(self, parsed_path: Path[ProductPath]) -> ProductResponse:
        """Return a product with a transformed image URL."""
        product_id = parsed_path.product_id
        source = f'https://originals.example.com/products/{product_id}.jpg'
        image = imgproxy_url(source, 'thumbnail')  # (1)!
        return ProductResponse(id=product_id, image=image)  # (2)!
