class ReplyKeyboardMarkup:
    keyboard : list[list[KeyboardButton]]
    is_persistent : bool
    resize_keyboard : bool
    one_time_keyboard : bool
    input_field_placeholder : str
    selective : bool
    def __init__(self,**kwargs):
        self.keyboard = [list[KeyboardButton](s) for s in kwargs.get('keyboard', [])]
        self.is_persistent = kwargs.get('is_persistent', False)
        self.resize_keyboard = kwargs.get('resize_keyboard', False)
        self.one_time_keyboard = kwargs.get('one_time_keyboard', False)
        self.input_field_placeholder = kwargs.get('input_field_placeholder', "")
        self.selective = kwargs.get('selective', False)