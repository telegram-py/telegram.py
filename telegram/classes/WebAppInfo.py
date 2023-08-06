class WebAppInfo:
    url: str

    def __init__(self, **kwargs):
        self.url = kwargs.get('url', "")
