from typing import Annotated

from fastapi import Depends, FastAPI

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()
get_public = add_imgproxy(
    app,
    Client('https://images.example.com'),
    name='public',  # (1)!
)
get_internal = add_imgproxy(
    app,
    Client('https://images.internal.example.com'),
    name='internal',
)


@app.get('/image')
async def get_image(
    public: Annotated[Client, Depends(get_public)],  # (2)!
    internal: Annotated[Client, Depends(get_internal)],
) -> dict[str, str]:
    """Generate URLs using two separately registered clients."""
    source = 'https://media.example.com/photo.jpg'
    return {'public': public.url(source), 'internal': internal.url(source)}
