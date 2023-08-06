class BotCommandScopeDefault:
    type: str

    def __init__(self, **kwargs):
        self.type = 'default'
        self.__dict__.update(kwargs)
