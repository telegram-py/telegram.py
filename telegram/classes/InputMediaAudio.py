from telegram.classes.InputFile import InputFile
from telegram.classes.MessageEntity import MessageEntity


class InputMediaAudio:
    type: str
    media: str
    thumb: InputFile
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    duration: int
    performer: str
    title: str

    def __init__(self, **kwargs):
        self.type = 'audio'
        self.media = str(kwargs.get('media', ''))
        self.thumb = InputFile(**kwargs.get('thumb', {}))
        self.caption = str(kwargs.get('caption', ''))
        self.parse_mode = str(kwargs.get('parse_mode', ''))
        self.caption_entities = [MessageEntity(**x) for x in kwargs.get('caption_entities', [])]
        self.duration = int(kwargs.get('duration', 0))
        self.performer = str(kwargs.get('performer', ''))
        self.title = str(kwargs.get('title', ''))
