from typing import Annotated, Final

from fastapi import Depends, FastAPI

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

_PREVIEW: Final = Transform(width=640, format='webp')


@app.get('/images')
async def image(
    source: str,
    imgproxy: Annotated[Client, Depends(get_imgproxy)],
) -> dict[str, str]:
    """Return an imgproxy URL for the requested source image."""
    return {'url': imgproxy.url(source, transform=_PREVIEW)}
