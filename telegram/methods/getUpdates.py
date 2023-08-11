import aiohttp
import asyncio
import json

async def getUpdates(**kwargs):
    data : {offset : int, limit : int, timeout : int, allowed_updates : list} = kwargs
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.telegram.org/bot{token}/getUpdates',data=data) as resp:
            return await resp.json()
