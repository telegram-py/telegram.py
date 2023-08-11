import aiohttp
import asyncio
from telegram.classes.MessageEntity import MessageEntity
async def sendMessage(chat_id : str | int ,text : str ,**kwargs):
    chat_id = str(chat_id)
    text = str(text)
    parse_mode = kwargs.get('parse_mode', None)
    entities = [MessageEntity(x) for x in kwargs.get('entities', None)]
    disable_web_page_preview = kwargs.get('disable_web_page_preview', None)
    disable_notification = kwargs.get('disable_notification', None)
    reply_to_message_id = kwargs.get('reply_to_message_id', None)
    allow_sending_without_reply = kwargs.get('allow_sending_without_reply', None)
    reply_markup = kwargs.get('reply_markup', None)
    params = {'chat_id':chat_id,'text':text,'parse_mode':parse_mode,'entities':entities,'disable_web_page_preview':disable_web_page_preview,'disable_notification':disable_notification,'reply_to_message_id':reply_to_message_id,'allow_sending_without_reply':allow_sending_without_reply,'reply_markup':reply_markup}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.telegram.org/bot'+token+'/sendMessage',data=params) as resp:
            return await resp.json()





    

