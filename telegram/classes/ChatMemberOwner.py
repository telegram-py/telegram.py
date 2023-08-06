from telegram.classes.User import User


class ChatMemberOwner:
    status: str
    user: User
    is_anonymous: bool
    custom_title: str

    def __init__(self, **kwargs):
        self.status = kwargs.get('status', "")
        self.user = User(**kwargs.get('user', dict()))
        self.is_anonymous = kwargs.get('is_anonymous', False)
        self.custom_title = kwargs.get('custom_title', "")
