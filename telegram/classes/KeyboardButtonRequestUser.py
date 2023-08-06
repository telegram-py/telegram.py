class KeyboardButtonRequestUser:
    request_id: int
    user_is_bot: bool
    user_is_premium: bool

    def __init__(self, **kwargs: dict) -> None:
        self.request_id = kwargs.get('request_id', 0)
        self.user_is_bot = kwargs.get('user_is_bot', False)
        self.user_is_premium = kwargs.get('user_is_premium', False)
