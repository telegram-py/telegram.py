class BotCommandScopeChatAdministrators:
    type: str
    chat_id: int

    def __init__(self, **kwargs):
        self.type = 'chat_administrators'
        self.chat_id = int(kwargs.get('chat_id', 0))
