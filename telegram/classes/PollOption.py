class PollOption:
    text: str
    voter_count: int

    def __init__(self, **kwargs):
        self.text = kwargs.get('text')
        self.voter_count = kwargs.get('voter_count')
