from telegram.classes.InputFile import InputFile
from telegram.classes.MessageEntity import MessageEntity


class InputMediaVideo:
    type: str
    media: str
    thumb: InputFile
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    width: int
    height: int
    duration: int
    supports_streaming: bool
    has_spoiler: bool

    def __init__(self, **kwargs):
        self.type = 'video'
        self.media = str(kwargs.get('media', ''))
        self.thumb = InputFile(**kwargs.get('thumb', {}))
        self.caption = str(kwargs.get('caption', ''))
        self.parse_mode = str(kwargs.get('parse_mode', ''))
        self.caption_entities = [MessageEntity(**x) for x in kwargs.get('caption_entities', [])]
        self.width = int(kwargs.get('width', 0))
        self.height = int(kwargs.get('height', 0))
        self.duration = int(kwargs.get('duration', 0))
        self.supports_streaming = bool(kwargs.get('supports_streaming', False))
        self.has_spoiler = bool(kwargs.get('has_spoiler', False))
