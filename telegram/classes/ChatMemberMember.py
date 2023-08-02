class ChatMemberMember:
    status : str
    user : User
    def __init__(self,**kwargs):
        self.status = kwargs.get('status', "")
        self.user = User(**kwargs.get('user', dict()))