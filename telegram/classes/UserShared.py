class UserShared:
    request_id: int
    user_id: int

    def __init__(self, **kwargs):
        self.request_id = kwargs.get('request_id', 0)
        self.user_id = kwargs.get('user_id', 0)
