class ChatInviteLink:
    invite_link : str
    creator : User
    creates_join_request : bool
    is_primary : bool
    is_revoked : bool
    name : str
    expire_date : int
    member_limit : int
    pending_join_request_count : int
    def __init__(self,**kwargs):
        self.invite_link = kwargs.get('invite_link', "")
        self.creator = User(**kwargs.get('creator', dict()))
        self.creates_join_request = kwargs.get('creates_join_request', False)
        self.is_primary = kwargs.get('is_primary', False)
        self.is_revoked = kwargs.get('is_revoked', False)
        self.name = kwargs.get('name', "")
        self.expire_date = kwargs.get('expire_date', 0)
        self.member_limit = kwargs.get('member_limit', 0)
        self.pending_join_request_count = kwargs.get('pending_join_request_count', 0)