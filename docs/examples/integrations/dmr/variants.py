from dmr import Controller, Path
from dmr.plugins.pydantic import PydanticFastSerializer
from pydantic import BaseModel

from imgproxykit.integrations.django import imgproxy_variants


class ProductPath(BaseModel):
    """Identify the product requested by the URL."""

    product_id: int


class ProductImages(BaseModel):
    """Named image variants exposed by the API."""

    small: str
    large: str


class ProductResponse(BaseModel):
    """Product and its named image variants."""

    id: int
    images: ProductImages  # (1)!


class ProductController(Controller[PydanticFastSerializer]):
    """Serve a product with its image variants."""

    def get(self, parsed_path: Path[ProductPath]) -> ProductResponse:
        """Return a product with its configured image variants."""
        product_id = parsed_path.product_id
        source = f'https://originals.example.com/products/{product_id}.jpg'
        images = imgproxy_variants(source, 'product')  # (2)!
        return ProductResponse(
            id=product_id,
            images=ProductImages(**images),  # (3)!
        )
