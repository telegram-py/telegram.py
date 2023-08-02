class BotName:
    name : str
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')