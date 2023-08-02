class ChatJoinRequest:
    chat : Chat
    from_user : User
    user_chat_id : int
    date : int
    bio : str
    invite_link : ChatInviteLink
    def __init__(self,**kwargs):
        self.chat = Chat(**kwargs.get('chat', dict()))
        self.from_user = User(**kwargs.get('from_user', dict()))
        self.user_chat_id = kwargs.get('user_chat_id', 0)
        self.date = kwargs.get('date', 0)
        self.bio = kwargs.get('bio', "")
        self.invite_link = ChatInviteLink(**kwargs.get('invite_link', dict()))