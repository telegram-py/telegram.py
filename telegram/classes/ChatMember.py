from telegram.classes.ChatMemberAdministrator import ChatMemberAdministrator
from telegram.classes.ChatMemberOwner import ChatMemberOwner
from telegram.classes.ChatMemberRestricted import ChatMemberRestricted
from telegram.classes.ChatMemberLeft import ChatMemberLeft
from telegram.classes.ChatMemberBanned import ChatMemberBanned
from telegram.classes.ChatMemberMember import ChatMemberMember
from telegram.classes.ChatMemberUpdated import ChatMemberUpdated


class ChatMember:
    type: str
    object: object

    def __init__(self, **kwargs):
        self.type = kwargs.get('type')
        if self.type == 'chat_member_administrator':
            self.object = ChatMemberAdministrator(**kwargs.get('object', dict()))
        elif self.type == 'chat_member_owner':
            self.object = ChatMemberOwner(**kwargs.get('object', dict()))
        elif self.type == 'chat_member_restricted':
            self.object = ChatMemberRestricted(**kwargs.get('object', dict()))
        elif self.type == 'chat_member_left':
            self.object = ChatMemberLeft(**kwargs.get('object', dict()))
        elif self.type == 'chat_member_banned':
            self.object = ChatMemberBanned(**kwargs.get('object', dict()))
        elif self.type == 'chat_member_member':
            self.object = ChatMemberMember(**kwargs.get('object', dict()))
        elif self.type == 'chat_member_updated':
            self.object = ChatMemberUpdated(**kwargs.get('object', dict()))
        else:
            self.object = None
