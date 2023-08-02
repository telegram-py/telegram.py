class InlineKeyboardMarkup:
    inline_keyboard : list[list[InlineKeyboardButton]]
    def __init__(self,**kwargs):
        self.inline_keyboard = [InlineKeyboardButton(x) for x in kwargs.get('inline_keyboard', list())]
        