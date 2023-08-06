class BotCommandScopeAllChatAdministrators:
    type: str

    def __init__(self, **kwargs):
        self.type = 'all_chat_administrators'
        self.__dict__.update(kwargs)
