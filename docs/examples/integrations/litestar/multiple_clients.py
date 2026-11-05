from litestar import Litestar, get
from litestar.di import NamedDependency

from imgproxykit import Client
from imgproxykit.integrations.litestar import ImgproxyPlugin


@get('/image')
async def get_image(
    public: NamedDependency[Client],  # (2)!
    internal: NamedDependency[Client],
) -> dict[str, str]:
    """Generate URLs using two separately registered clients."""
    source = 'https://media.example.com/photo.jpg'
    return {'public': public.url(source), 'internal': internal.url(source)}


app = Litestar(
    route_handlers=[get_image],
    plugins=[
        ImgproxyPlugin(
            clients={
                'public': Client('https://images.example.com'),  # (1)!
                'internal': Client('https://images.internal.example.com'),
            }
        ),
    ],
)
