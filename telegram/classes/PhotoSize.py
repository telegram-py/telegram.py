class PhotoSize:
    file_id : str
    file_unique_id : str
    width : int
    height : int
    file_size : int
    
    def __init__(self, **kwargs):
        self.file_id: str = kwargs.get('file_id', '')
        self.file_unique_id: str = kwargs.get('file_unique_id', '')
        self.width: int = int(kwargs.get('width', 0))
        self.height: int = int(kwargs.get('height', 0))
        self.file_size: int = int(kwargs.get('file_size', 0))