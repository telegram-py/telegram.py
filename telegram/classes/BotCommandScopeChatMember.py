class BotCommandScopeChatMember:
    type: str
    chat_id: int
    user_id: int

    def __init__(self, **kwargs):
        self.type = 'chat_member'
        self.chat_id = int(kwargs.get('chat_id', 0))
        self.user_id = int(kwargs.get('user_id', 0))
