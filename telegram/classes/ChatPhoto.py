class ChatPhoto:
    small_file_id : str
    small_file_unique_id : str
    big_file_id : str
    big_file_unique_id : str
    def __init__(self,**kwargs):
        self.small_file_id = kwargs.get('small_file_id', "")
        self.small_file_unique_id = kwargs.get('small_file_unique_id', "")
        self.big_file_id = kwargs.get('big_file_id', "")
        self.big_file_unique_id = kwargs.get('big_file_unique_id', "")