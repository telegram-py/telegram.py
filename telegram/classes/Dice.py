class Dice:
    emoji: str
    value: int
    def __init__(self, **kwargs):
        self.emoji = kwargs.get('emoji')
        self.value = kwargs.get('value')
