from telegram.classes.User import User


class ChatMemberBanned:
    status: str
    user: User
    until_date: int

    def __init__(self, **kwargs):
        self.status = kwargs.get('status', "")
        self.user = User(**kwargs.get('user', dict()))
        self.until_date = kwargs.get('until_date', 0)
