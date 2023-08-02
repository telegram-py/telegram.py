class VideoChatParticipantsInvited:
    users : list[User]
    def __init__(self,**kwargs):
        self.users = [User(s) for s in kwargs.get('users', [])]
