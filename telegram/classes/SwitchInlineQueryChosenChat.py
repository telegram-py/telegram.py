class SwitchInlineQueryChosenChat:
    query: str
    allow_user_chats: bool
    allow_bot_chats: bool
    allow_group_chats: bool
    allow_channel_chats: bool

    def __init__(self, **kwargs):
        self.query = kwargs.get('query', "")
        self.allow_user_chats = kwargs.get('allow_user_chats', False)
        self.allow_bot_chats = kwargs.get('allow_bot_chats', False)
        self.allow_group_chats = kwargs.get('allow_group_chats', False)
        self.allow_channel_chats = kwargs.get('allow_channel_chats', False)
