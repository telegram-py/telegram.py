from telegram.classes.User import User


class PollAnswer:
    poll_id: str
    user: User
    option_ids: list[int]

    def __init__(self, **kwargs):
        self.poll_id = kwargs.get('poll_id')
        self.user = User(**kwargs.get('user'))
        self.option_ids = kwargs.get('option_ids')
