class Animation:
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumbnail: PhotoSize
    file_name: str
    mime_type: str
    file_size: int

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id', '')
        self.file_unique_id = kwargs.get('file_unique_id', '')
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.duration = kwargs.get('duration', 0)
        self.thumbnail = PhotoSize(**kwargs.get('thumbnail', None))
        self.file_name = kwargs.get('file_name', None)
        self.mime_type = kwargs.get('mime_type', None)
        self.file_size = kwargs.get('file_size', None)