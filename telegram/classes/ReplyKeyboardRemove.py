class ReplyKeyboardRemove:
    remove_keyboard: bool
    selective: bool

    def __init__(self, **kwargs):
        self.remove_keyboard = kwargs.get('remove_keyboard', False)
        self.selective = kwargs.get('selective', False)
