class MessageEntity:
    type : str
    offset : int
    length : int
    url : str
    user : User
    language : str
    custom_emoji_id : str
    def __init__(self, **kwargs):
        self.type = kwargs.get('entity_type', None)
        self.offset = kwargs.get('offset', None)
        self.length = kwargs.get('length', None)
        self.url = kwargs.get('url', None)
        self.user = User(**kwargs.get('user', None))
        self.language = kwargs.get('language', None)
        self.custom_emoji_id = kwargs.get('custom_emoji_id', None)