"""
Register an additional client under a separate state attribute.

>>> import asyncio
>>> from fastapi import Request
>>> async def example():
...     request = Request({'type': 'http', 'app': app})
...     default = await get_imgproxy(request)
...     preview = await get_preview_imgproxy(request)
...     return default, preview
>>> default, preview = asyncio.run(example())
>>> default is app.state.imgproxykit_client
True
>>> preview is app.state.preview_imgproxy_client
True
>>> preview.url('s3://images/photo.jpg').startswith(
...     'https://preview-imgproxy.example.com/'
... )
True
"""

from fastapi import FastAPI

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()
get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))

get_preview_imgproxy = add_imgproxy(
    app,
    Client('https://preview-imgproxy.example.com'),
    name='preview_imgproxy_client',
)
