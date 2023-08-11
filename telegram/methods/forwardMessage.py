async def forward_message(chat_id: str, from_chat_id: str, message_id: int,**kwargs):
    chat_id = str(chat_id)
    from_chat_id = str(from_chat_id)
    message_id = str(message_id)
    message_thread_id = kwargs.get('message_thread_id', None)
    disable_notification = kwargs.get('disable_notification', None)
    protect_content = kwargs.get('protect_content', None)
    params = {
              'chat_id':chat_id,
              'from_chat_id':from_chat_id,
              'message_id':message_id,
              'message_thread_id':message_thread_id,
              'disable_notification':disable_notification,
              'protect_content':protect_content
              }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.telegram.org/bot'+token+'/forwardMessage',data=params) as resp:
            return await resp.json()