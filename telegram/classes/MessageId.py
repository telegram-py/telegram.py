class MessageId:
    id: int

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
