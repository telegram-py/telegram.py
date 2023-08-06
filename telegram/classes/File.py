class File:
    file_id: str
    file_unique_id: str
    file_size: int
    file_path: str

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id', "")
        self.file_unique_id = kwargs.get('file_unique_id', "")
        self.file_size = kwargs.get('file_size', 0)
        self.file_path = kwargs.get('file_path', "")
