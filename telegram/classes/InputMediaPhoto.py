from telegram.classes.MessageEntity import MessageEntity


class InputMediaPhoto:
    type: str
    media: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    has_spoiler: bool

    def __init__(self, **kwargs):
        self.type = 'photo'
        self.media = str(kwargs.get('media', ''))
        self.caption = str(kwargs.get('caption', ''))
        self.parse_mode = str(kwargs.get('parse_mode', ''))
        self.caption_entities = [MessageEntity(**x) for x in kwargs.get('caption_entities', [])]
        self.has_spoiler = bool(kwargs.get('has_spoiler', False))
