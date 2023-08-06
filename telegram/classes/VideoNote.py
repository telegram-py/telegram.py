from telegram.classes.PhotoSize import PhotoSize


class VideoNote:
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumbnail: PhotoSize
    file_size: int

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id')
        self.file_unique_id = kwargs.get('file_unique_id')
        self.length = kwargs.get('length')
        self.duration = kwargs.get('duration')
        self.thumbnail = PhotoSize(**kwargs.get('thumbnail'))
        self.file_size = kwargs.get('file_size')
