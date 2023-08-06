from telegram.classes.PhotoSize import PhotoSize
from telegram.classes.File import File
from telegram.classes.MaskPosition import MaskPosition


class Sticker:
    file_id: str
    file_unique_id: str
    type: str
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumb: PhotoSize
    emoji: str
    set_name: str
    premium_animation: File
    mask_position: MaskPosition
    custom_emoji_id: str
    needs_repainting: bool
    file_size: int

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id', '')
        self.file_unique_id = kwargs.get('file_unique_id', '')
        self.type = kwargs.get('type', '')
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.is_animated = kwargs.get('is_animated', False)
        self.is_video = kwargs.get('is_video', False)
        self.thumb = PhotoSize(**kwargs.get('thumb', {}))
        self.emoji = kwargs.get('emoji', '')
        self.set_name = kwargs.get('set_name', '')
        self.premium_animation = File(**kwargs.get('premium_animation', {}))
        self.mask_position = MaskPosition(**kwargs.get('mask_position', {}))
        self.custom_emoji_id = kwargs.get('custom_emoji_id', '')
        self.needs_repainting = kwargs.get('needs_repainting', False)
        self.file_size = kwargs.get('file_size', 0)
