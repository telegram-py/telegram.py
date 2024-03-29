from telegram.classes.Game import Game
from telegram.classes.Invoice import Invoice
from telegram.classes.Animation import Animation
from telegram.classes.Audio import Audio
from telegram.classes.Chat import Chat
from telegram.classes.Contact import Contact
from telegram.classes.Dice import Dice
from telegram.classes.ForumTopicClosed import ForumTopicClosed
from telegram.classes.ForumTopicCreated import ForumTopicCreated
from telegram.classes.ForumTopicEdited import ForumTopicEdited
from telegram.classes.InlineKeyboardMarkup import InlineKeyboardMarkup
from telegram.classes.Location import Location
from telegram.classes.MessageAutoDeleteTimerChanged import MessageAutoDeleteTimerChanged
from telegram.classes.MessageEntity import MessageEntity
from telegram.classes.PhotoSize import PhotoSize
from telegram.classes.Poll import Poll
from telegram.classes.User import User
from telegram.classes.Venue import Venue
from telegram.classes.Video import Video
from telegram.classes.VideoChatEnded import VideoChatEnded
from telegram.classes.VideoChatParticipantsInvited import VideoChatParticipantsInvited
from telegram.classes.VideoChatScheduled import VideoChatScheduled
from telegram.classes.VideoChatStarted import VideoChatStarted
from telegram.classes.VideoNote import VideoNote
from telegram.classes.Voice import Voice
from telegram.classes.Document import Document
from telegram.classes.Sticker import Sticker
from telegram.classes.SuccessfulPayment import SuccessfulPayment
from telegram.classes.PassportData import PassportData
from telegram.classes.ForumTopicReopened import ForumTopicReopened
from telegram.classes.ProximityAlertTriggered import ProximityAlertTriggered
from telegram.classes.GeneralForumTopicHidden import GeneralForumTopicHidden
from telegram.classes.GeneralForumTopicUnhidden import GeneralForumTopicUnhidden


class Message:
    message_id: int
    message_thread_id: int
    from_user: User
    sender_chat: Chat
    date: int
    chat: Chat
    forward_from: User
    forward_from_chat: Chat
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: int
    is_topic_message: bool
    is_automatic_forward: bool
    reply_to_message: 'Message'
    via_bot: User
    edit_date: int
    has_protected_content: bool
    media_group_id: str
    author_signature: str
    text: str
    entities: list[MessageEntity]
    animation: Animation
    audio: Audio
    document: Document
    photo: list[PhotoSize]
    sticker: Sticker
    video: Video
    video_note: VideoNote
    voice: Voice
    caption: str
    caption_entities: list[MessageEntity]
    has_media_spoiler: bool
    contact: Contact
    dice: Dice
    game: Game
    poll: Poll
    venue: Venue
    location: Location
    new_chat_members: list[User]
    left_chat_member: User
    new_chat_title: str
    new_chat_photo: list[PhotoSize]
    delete_chat_photo: bool
    group_chat_created: bool
    supergroup_chat_created: bool
    channel_chat_created: bool
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged
    migrate_to_chat_id: int
    migrate_from_chat_id: int
    pinned_message: 'Message'
    invoice: Invoice
    successful_payment: SuccessfulPayment
    user_shared: bool
    chat_shared: bool
    connected_website: str
    write_access_allowed: bool
    passport_data: PassportData
    proximity_alert_triggered: ProximityAlertTriggered
    forum_topic_created: ForumTopicCreated
    forum_topic_edited: ForumTopicEdited
    forum_topic_closed: ForumTopicClosed
    forum_topic_reopened: ForumTopicReopened
    general_forum_topic_hidden: GeneralForumTopicHidden
    general_forum_topic_unhidden: GeneralForumTopicUnhidden
    video_chat_scheduled: VideoChatScheduled
    video_chat_started: VideoChatStarted
    video_chat_ended: VideoChatEnded
    video_chat_participants_invited: VideoChatParticipantsInvited
    web_app_data: str
    reply_markup: InlineKeyboardMarkup

    def __init__(self, **kwargs):
        self.message_id = kwargs.get('message_id')
        self.message_thread_id = kwargs.get('message_thread_id')
        self.from_user = User(**kwargs.get('from_user'))
        self.sender_chat = kwargs.get('sender_chat')
        self.date = kwargs.get('date')
        self.chat = Chat(**kwargs.get('chat'))
        self.forward_from = User(**kwargs.get('forward_from'))
        self.forward_from_chat = Chat(**kwargs.get('forward_from_chat'))
        self.forward_from_message_id = kwargs.get('forward_from_message_id')
        self.forward_signature = kwargs.get('forward_signature')
        self.forward_sender_name = kwargs.get('forward_sender_name')
        self.forward_date = kwargs.get('forward_date')
        self.is_topic_message = kwargs.get('is_topic_message')
        self.is_automatic_forward = kwargs.get('is_automatic_forward')
        self.reply_to_message = Message(**kwargs.get('reply_to_message'))
        self.via_bot = User(**kwargs.get('via_bot'))
        self.edit_date = kwargs.get('edit_date')
        self.has_protected_content = kwargs.get('has_protected_content')
        self.media_group_id = kwargs.get('media_group_id')
        self.author_signature = kwargs.get('author_signature')
        self.text = kwargs.get('text')
        self.entities = [MessageEntity(**entity) for entity in kwargs.get('entities')]
        self.animation = Animation(**kwargs.get('animation'))
        self.audio = Audio(**kwargs.get('audio'))
        self.document = Document(**kwargs.get('document'))
        self.photo = [PhotoSize(**photo) for photo in kwargs.get('photo')]
        self.sticker = Sticker(**kwargs.get('sticker'))
        self.video = Video(**kwargs.get('video'))
        self.video_note = VideoNote(**kwargs.get('video_note'))
        self.voice = Voice(**kwargs.get('voice'))
        self.caption = kwargs.get('caption')
        self.caption_entities = [MessageEntity(**entity) for entity in kwargs.get('caption_entities')]
        self.has_media_spoiler = kwargs.get('has_media_spoiler')
        self.contact = Contact(**kwargs.get('contact'))
        self.dice = Dice(**kwargs.get('dice'))
        self.game = Game(**kwargs.get('game'))
        self.poll = Poll(**kwargs.get('poll'))
        self.venue = Venue(**kwargs.get('venue'))
        self.location = Location(**kwargs.get('location'))
        self.new_chat_members = [User(**user) for user in kwargs.get('new_chat_members')]
        self.left_chat_member = User(**kwargs.get('left_chat_member'))
        self.new_chat_title = kwargs.get('new_chat_title')
        self.new_chat_photo = [PhotoSize(**photo) for photo in kwargs.get('new_chat_photo')]
        self.delete_chat_photo = kwargs.get('delete_chat_photo')
        self.group_chat_created = kwargs.get('group_chat_created')
        self.supergroup_chat_created = kwargs.get('supergroup_chat_created')
        self.channel_chat_created = kwargs.get('channel_chat_created')
        self.message_auto_delete_timer_changed = MessageAutoDeleteTimerChanged(
            **kwargs.get('message_auto_delete_timer_changed'))
        self.migrate_to_chat_id = kwargs.get('migrate_to_chat_id')
        self.migrate_from_chat_id = kwargs.get('migrate_from_chat_id')
        self.pinned_message = Message(**kwargs.get('pinned_message'))
        self.invoice = Invoice(**kwargs.get('invoice'))
        self.successful_payment = SuccessfulPayment(**kwargs.get('successful_payment'))
        self.user_shared = kwargs.get('user_shared')
        self.chat_shared = kwargs.get('chat_shared')
        self.connected_website = kwargs.get('connected_website')
        self.write_access_allowed = kwargs.get('write_access_allowed')
        self.passport_data = PassportData(**kwargs.get('passport_data'))
        self.proximity_alert_triggered = ProximityAlertTriggered(**kwargs.get('proximity_alert_triggered'))
        self.forum_topic_created = ForumTopicCreated(**kwargs.get('forum_topic_created'))
        self.forum_topic_edited = ForumTopicEdited(**kwargs.get('forum_topic_edited'))
        self.forum_topic_closed = ForumTopicClosed(**kwargs.get('forum_topic_closed'))
        self.forum_topic_reopened = ForumTopicReopened(**kwargs.get('forum_topic_reopened'))
        self.general_forum_topic_hidden = GeneralForumTopicHidden(**kwargs.get('general_forum_topic_hidden'))
        self.general_forum_topic_unhidden = GeneralForumTopicUnhidden(**kwargs.get('general_forum_topic_unhidden'))
        self.video_chat_scheduled = VideoChatScheduled(**kwargs.get('video_chat_scheduled'))
        self.video_chat_started = VideoChatStarted(**kwargs.get('video_chat_started'))
        self.video_chat_ended = VideoChatEnded(**kwargs.get('video_chat_ended'))
        self.video_chat_participants_invited = VideoChatParticipantsInvited(
            **kwargs.get('video_chat_participants_invited'))
        self.web_app_data = kwargs.get('web_app_data')
        self.reply_markup = InlineKeyboardMarkup(**kwargs.get('reply_markup'))
