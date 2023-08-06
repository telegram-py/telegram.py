from telegram.classes.KeyBoardButtonPollType import KeyboardButtonPollType
from telegram.classes.KeyboardButtonRequestChat import KeyboardButtonRequestChat
from telegram.classes.KeyboardButtonRequestUser import KeyboardButtonRequestUser
from telegram.classes.WebAppInfo import WebAppInfo


class KeyboardButton:
    text: str
    request_user: KeyboardButtonRequestUser
    request_chat: KeyboardButtonRequestChat
    request_contact: bool
    request_location: bool
    request_poll = KeyboardButtonPollType
    web_app: WebAppInfo

    def __init__(self, **kwargs):
        self.text = kwargs.get('text', "")
        self.request_user = KeyboardButtonRequestUser(**kwargs.get('request_user', dict()))
        self.request_chat = KeyboardButtonRequestChat(**kwargs.get('request_chat', dict()))
        self.request_contact = kwargs.get('request_contact', False)
        self.request_location = kwargs.get('request_location', False)
        self.request_poll = KeyboardButtonPollType(**kwargs.get('request_poll', dict()))
        self.web_app = WebAppInfo(**kwargs.get('web_app', dict()))
