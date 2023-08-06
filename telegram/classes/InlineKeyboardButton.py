from telegram.classes.LoginUrl import LoginUrl
from telegram.classes.WebAppInfo import WebAppInfo
from telegram.classes.SwitchInlineQueryChosenChat import SwitchInlineQueryChosenChat
from telegram.classes.CallbackGame import CallbackGame


class InlineKeyboardButton:
    text: str
    url: str
    callback_data: str
    web_app: WebAppInfo
    login_url: LoginUrl
    switch_inline_query: str
    switch_inline_query_current_chat: str
    switch_inline_query_chosen_chat: SwitchInlineQueryChosenChat
    callback_game: CallbackGame
    pay: bool

    def __init__(self, **kwargs):
        self.text = kwargs.get('text', "")
        self.url = kwargs.get('url', "")
        self.callback_data = kwargs.get('callback_data', "")
        self.web_app = WebAppInfo(**kwargs.get('web_app', dict()))
        self.login_url = LoginUrl(**kwargs.get('login_url', dict()))
        self.switch_inline_query = kwargs.get('switch_inline_query', "")
        self.switch_inline_query_current_chat = kwargs.get('switch_inline_query_current_chat', "")
        self.switch_inline_query_chosen_chat = SwitchInlineQueryChosenChat(
            **kwargs.get('switch_inline_query_chosen_chat', dict()))
        self.callback_game = CallbackGame(**kwargs.get('callback_game', dict()))
        self.pay = kwargs.get('pay', False)
