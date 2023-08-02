class Audio:
    file_id: str
    file_unique_id: str
    duration: int
    performer: str
    title: str
    file_name: str
    mime_type: str
    file_size: int
    thumbnail: PhotoSize
    def __init__(self, **kwargs):
        self.file_id: str = kwargs.get('file_id', '')
        self.file_unique_id: str = kwargs.get('file_unique_id', '')
        self.duration: int = kwargs.get('duration', 0)
        self.performer: str = kwargs.get('performer', None)
        self.title: str = kwargs.get('title', None)
        self.file_name: str = kwargs.get('file_name', None)
        self.mime_type: str = kwargs.get('mime_type', None)
        self.file_size: int = kwargs.get('file_size', None)
        self.thumbnail: PhotoSize = PhotoSize(**kwargs.get('thumbnail', None))