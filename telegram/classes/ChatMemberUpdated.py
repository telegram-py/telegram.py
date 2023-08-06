from telegram.classes.ChatInviteLink import ChatInviteLink
from telegram.classes.Chat import Chat
from telegram.classes.User import User
from telegram.classes.ChatMember import ChatMember


class ChatMemberUpdated:
    chat: Chat
    from_user: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: ChatInviteLink

    def __init__(self, **kwargs):
        self.chat = Chat(**kwargs.get('chat', dict()))
        self.from_user = User(**kwargs.get('from_user', dict()))
        self.date = kwargs.get('date', 0)
        self.old_chat_member = ChatMember(**kwargs.get('old_chat_member', dict()))
        self.new_chat_member = ChatMember(**kwargs.get('new_chat_member', dict()))
        self.invite_link = ChatInviteLink(**kwargs.get('invite_link', dict()))
