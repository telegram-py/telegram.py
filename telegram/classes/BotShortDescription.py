class BotShortDescription:
    short_description : str
    def __init__(self, **kwargs):
        self.short_description = str(kwargs.get('short_description', ''))