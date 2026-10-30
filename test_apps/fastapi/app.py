from dataclasses import dataclass
from typing import Annotated, Final

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from imgproxykit import Client, Transform
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()

# Match the local imgproxy service configured in docker-compose.yaml.
get_imgproxy = add_imgproxy(
    app,
    Client(
        'http://localhost:10002',
        key='736563726574',
        salt='73616c74',
    ),
)

_BASE: Final = Transform(format='webp')
_THUMBNAIL: Final = _BASE.extend(width=320)
_PREVIEW: Final = _BASE.extend(width=640)


@dataclass(frozen=True, slots=True)
class _Variants:
    thumbnail: Annotated[str, _THUMBNAIL]
    preview: Annotated[str, _PREVIEW]


class VariantsResponse(BaseModel):
    """Serialize typed image variants inside a response DTO."""

    images: _Variants


@app.get('/images')
async def image(
    source: str,
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> dict[str, str]:
    """Return an imgproxy URL for the requested source image."""
    return {'url': imgproxy.url(source, transform=_PREVIEW)}


@app.get('/images/variants')
async def image_variants(
    source: str,
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> VariantsResponse:
    """Return typed imgproxy variants for the requested source image."""
    return VariantsResponse(
        images=imgproxy.variants(source, variants=_Variants),
    )
