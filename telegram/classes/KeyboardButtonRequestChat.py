from telegram.classes.ChatAdministratorRights import ChatAdministratorRights


class KeyboardButtonRequestChat:
    request_id: int
    chat_is_channel: bool
    chat_is_forum: bool
    chat_has_username: bool
    chat_is_created: bool
    user_administration_rights: ChatAdministratorRights
    bot_administration_rights: ChatAdministratorRights
    bot_is_member: bool

    def __init__(self, **kwargs):
        self.request_id = kwargs.get('request_id', 0)
        self.chat_is_channel = kwargs.get('chat_is_channel', False)
        self.chat_is_forum = kwargs.get('chat_is_forum', False)
        self.chat_has_username = kwargs.get('chat_has_username', False)
        self.user_administration_rights = ChatAdministratorRights(**kwargs.get('user_administration_rights', dict()))
        self.bot_administration_rights = ChatAdministratorRights(**kwargs.get('bot_administration_rights', dict()))
        self.bot_is_member = kwargs.get('bot_is_member', False)
