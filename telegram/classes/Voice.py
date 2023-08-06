class Voice:
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str
    file_size: int

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id')
        self.file_unique_id = kwargs.get('file_unique_id')
        self.duration = kwargs.get('duration')
        self.mime_type = kwargs.get('mime_type')
        self.file_size = kwargs.get('file_size')
