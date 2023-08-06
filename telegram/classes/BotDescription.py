class BotDescription:
    description: str

    def __init__(self, **kwargs):
        self.description = str(kwargs.get('description', ''))
