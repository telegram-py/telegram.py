class WriteAccessAllowed:
    web_app_name: str

    def __init__(self, **kwargs):
        self.web_app_name = kwargs.get('web_app_name', "")
