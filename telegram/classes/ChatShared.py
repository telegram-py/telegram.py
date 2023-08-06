class ChatShared:
    request_id: int
    chat_id: int

    def __init__(self, **kwargs):
        self.request_id = kwargs.get('request_id', 0)
        self.chat_id = kwargs.get('chat_id', 0)
