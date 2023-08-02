class BotCommand:
    command : str
    description : str
    def __init__(self,**kwargs):
        self.command = kwargs.get('command', "")
        self.description = kwargs.get('description', "")