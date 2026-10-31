from django.db import models
from django.shortcuts import get_object_or_404
from dmr import Controller, Path
from dmr.plugins.pydantic import PydanticFastSerializer
from pydantic import BaseModel

from imgproxykit.integrations.django import imgproxy_url


class Product(models.Model):
    """Product with an optional uploaded image."""

    image = models.ImageField(upload_to='products/', blank=True)

    class Meta:
        app_label = 'products'


class ProductPath(BaseModel):
    """Identify the requested product."""

    product_id: int


class ProductResponse(BaseModel):
    """Product with an optional image URL."""

    id: int
    image: str | None


class ProductController(Controller[PydanticFastSerializer]):
    """Serve a product with its image URL."""

    def get(self, parsed_path: Path[ProductPath]) -> ProductResponse:
        """Return a product and transform its image when present."""
        product = get_object_or_404(Product, pk=parsed_path.product_id)
        return ProductResponse(
            id=product.pk,
            image=(
                imgproxy_url(product.image, 'thumbnail')
                if product.image  # (1)!
                else None
            ),
        )
