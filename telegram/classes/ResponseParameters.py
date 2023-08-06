class ResponseParameters:
    migrate_to_chat_id: int
    retry_after: int

    def __init__(self, **kwargs):
        self.migrate_to_chat_id = int(kwargs.get('migrate_to_chat_id', 0))
        self.retry_after = int(kwargs.get('retry_after', 0))
