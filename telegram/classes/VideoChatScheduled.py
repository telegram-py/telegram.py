class VideoChatScheduled:
    start_date : int
    def __init__(self,**kwargs):
        self.start_date = kwargs.get('start_date', 0)
