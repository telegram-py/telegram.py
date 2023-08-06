class VideoChatEnded:
    duration: int

    def __init__(self, **kwargs):
        self.duration = kwargs.get('duration', 0)
