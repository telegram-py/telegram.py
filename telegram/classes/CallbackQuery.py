class CallbackQuery:
    id : str
    from_user : User
    message : Message
    inline_message_id : str
    chat_instance : str
    data : str
    game_short_name : str
    def __init__(self,**kwargs):
        self.id = kwargs.get('id', "")
        self.from_user = User(**kwargs.get('from_user', dict()))
        self.message = Message(**kwargs.get('message', dict()))
        self.inline_message_id = kwargs.get('inline_message_id', "")
        self.chat_instance = kwargs.get('chat_instance', "")
        self.data = kwargs.get('data', "")
        self.game_short_name = kwargs.get('game_short_name', "")