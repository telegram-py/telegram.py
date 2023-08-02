class BotCommandScopeChat:
    type: str
    chat_id: int
    def __init__(self, **kwargs):
        self.type = 'chat'
        self.chat_id = int(kwargs.get('chat_id', 0))