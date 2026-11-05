from litestar import Litestar

from imgproxykit import Client
from imgproxykit.integrations.litestar import ImgproxyPlugin

client = Client('https://imgproxy.example.com')
app = Litestar(plugins=[ImgproxyPlugin(client)])
