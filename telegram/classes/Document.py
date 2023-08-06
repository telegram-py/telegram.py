from telegram.classes.PhotoSize import PhotoSize


class Document:
    file_id: str
    file_unique_id: str
    thumbnail: PhotoSize
    file_name: str
    mime_type: str
    file_size: int

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id')
        self.file_unique_id = kwargs.get('file_unique_id')
        self.thumbnail = kwargs.get('thumbnail')
        self.file_name = kwargs.get('file_name')
        self.mime_type = kwargs.get('mime_type')
        self.file_size = kwargs.get('file_size')
