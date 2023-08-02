class MenuButtonWebApp:
    type : str
    text : str
    web_app : WebAppInfo
    def __init__(self, **kwargs):
        self.type = 'web_app'
        self.text = str(kwargs.get('text', ''))
        self.web_app = WebAppInfo(**kwargs.get('web_app', {}))