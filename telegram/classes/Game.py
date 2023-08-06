from telegram.classes.PhotoSize import PhotoSize
from telegram.classes.MessageEntity import MessageEntity
from telegram.classes.Animation import Animation


class Game:
    title: str
    description: str
    photo: list[PhotoSize]
    text: str
    text_entities: list[MessageEntity]
    animation: Animation

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.description = kwargs.get('description', '')
        self.photo = [PhotoSize(**s) for s in kwargs.get('photo', [])]
        self.text = kwargs.get('text', '')
        self.text_entities = [MessageEntity(**s) for s in kwargs.get('text_entities', [])]
        self.animation = Animation(**kwargs.get('animation', {}))
