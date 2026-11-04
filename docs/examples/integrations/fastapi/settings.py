from fastapi import FastAPI

from imgproxykit import Client
from imgproxykit.integrations.fastapi import add_imgproxy

app = FastAPI()
get_imgproxy = add_imgproxy(app, Client('https://imgproxy.example.com'))
