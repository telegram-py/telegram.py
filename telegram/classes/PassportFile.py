class PassportFile:
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int

    def __init__(self, **kwargs):
        self.file_id = kwargs.get('file_id', '')
        self.file_unique_id = kwargs.get('file_unique_id', '')
        self.file_size = kwargs.get('file_size', 0)
        self.file_date = kwargs.get('file_date', 0)
