from telegram.classes.ChatPhoto import ChatPhoto
from telegram.classes.Message import Message
from telegram.classes.ChatPermissions import ChatPermissions
from telegram.classes.ChatLocation import ChatLocation


class Chat:
    id: int
    type: str
    title: str
    username: str
    first_name: str
    last_name: str
    is_forum: bool
    photo: ChatPhoto
    active_usernames: list
    emoji_status_custom_emoji_id: str
    bio: str
    has_private_forwards: bool
    has_restricted_voice_and_video_messages: bool
    join_to_send_messages: bool
    join_by_request: bool
    description: str
    invite_link: str
    pinned_message: Message
    permissions: ChatPermissions
    slow_mode_delay: int
    message_auto_delete_time: int
    has_aggressive_anti_spam_enabled: bool
    has_hidden_members: bool
    has_protected_content: bool
    sticker_set_name: str
    can_set_sticker_set: bool
    linked_chat_id: int
    location: ChatLocation

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.type = kwargs.get('type')
        self.title = kwargs.get('title')
        self.username = kwargs.get('username')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.is_forum = kwargs.get('is_forum')
        self.photo = ChatPhoto(**kwargs.get('photo'))
        self.active_usernames = kwargs.get('active_usernames')
        self.emoji_status_custom_emoji_id = kwargs.get('emoji_status_custom_emoji_id')
        self.bio = kwargs.get('bio')
        self.has_private_forwards = kwargs.get('has_private_forwards')
        self.has_restricted_voice_and_video_messages = kwargs.get('has_restricted_voice_and_video_messages')
        self.join_to_send_messages = kwargs.get('join_to_send_messages')
        self.join_by_request = kwargs.get('join_by_request')
        self.description = kwargs.get('description')
        self.invite_link = kwargs.get('invite_link')
        self.pinned_message = Message(**kwargs.get('pinned_message'))
        self.permissions = ChatPermissions(**kwargs.get('permissions'))
        self.slow_mode_delay = kwargs.get('slow_mode_delay')
        self.message_auto_delete_time = kwargs.get('message_auto_delete_time')
        self.has_aggressive_anti_spam_enabled = kwargs.get('has_aggressive_anti_spam_enabled')
        self.has_hidden_members = kwargs.get('has_hidden_members')
        self.has_protected_content = kwargs.get('has_protected_content')
        self.sticker_set_name = kwargs.get('sticker_set_name')
        self.can_set_sticker_set = kwargs.get('can_set_sticker_set')
        self.linked_chat_id = kwargs.get('linked_chat_id')
        self.location = ChatLocation(**kwargs.get('location'))
