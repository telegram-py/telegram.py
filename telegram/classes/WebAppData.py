class WebAppData:
    data : str
    button_text : str
    def __init__(self,**kwargs):
        self.data = kwargs.get('data')
        self.button_text = kwargs.get('button_text')
    