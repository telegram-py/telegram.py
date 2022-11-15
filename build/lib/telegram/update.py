import asyncio
import time

import aiohttp.web
from aiohttp import web,request
from pyngrok import ngrok
from .response import get_request
from .Commands import Commands

loop = asyncio.new_event_loop()


class Server:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    @staticmethod
    async def hello(request : aiohttp.web.Request):
        ok = Commands(await request.json())
        print(await request.json())
        print(time.time())
        return web.Response(200)

    async def run(self):
        app = web.Application()
        ngrok.kill(ngrok.get_ngrok_process())
        #http_tunnel = ngrok.connect(8443, bind_tls=True)
        url = ngrok.get_tunnels()
        print(url)
        baseurl = self.base_url + self.token + f"/setWebhook?url={url}&drop_pending_updates=True"
        ok = await get_request(baseurl)
        print(ok)
        app.add_routes([web.post('/', self.hello)])
        return app
