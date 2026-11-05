from dataclasses import dataclass
from typing import Annotated, Final

from litestar import Litestar, get
from litestar.di import NamedDependency
from litestar.params import FromQuery

from imgproxykit import Client, Transform
from imgproxykit.integrations.litestar import ImgproxyPlugin

_BASE: Final = Transform(format='webp')
_THUMBNAIL: Final = _BASE.extend(width=320)
_PREVIEW: Final = _BASE.extend(width=640)


@dataclass(frozen=True, slots=True)
class _Variants:
    thumbnail: Annotated[str, _THUMBNAIL]
    preview: Annotated[str, _PREVIEW]


@dataclass(frozen=True, slots=True)
class VariantsResponse:
    """Serialize typed image variants inside a response DTO."""

    images: _Variants


@get('/images')
async def image(
    source: FromQuery[str],
    imgproxy: NamedDependency[Client],
) -> dict[str, str]:
    """Return an imgproxy URL for the requested source image."""
    return {'url': imgproxy.url(source, transform=_PREVIEW)}


@get('/images/variants')
async def image_variants(
    source: FromQuery[str],
    imgproxy: NamedDependency[Client],
) -> VariantsResponse:
    """Return typed imgproxy variants for the requested source image."""
    images = imgproxy.variants(source, variants=_Variants)
    return VariantsResponse(images=images)


# Match the local imgproxy service configured in docker-compose.yaml.
app = Litestar(
    route_handlers=[image, image_variants],
    plugins=[
        ImgproxyPlugin(
            Client(
                'http://localhost:10002',
                key='736563726574',
                salt='73616c74',
            ),
        ),
    ],
)
