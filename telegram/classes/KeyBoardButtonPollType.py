class KeyboardButtonPollType:
    type : str
    def __init__(self,**kwargs):
        self.type = kwargs.get('type', "")
        