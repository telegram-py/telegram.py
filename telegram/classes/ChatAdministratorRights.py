class ChatAdministratorRights:
    is_anonymous : bool
    can_manage_chat : bool
    can_delete_messages : bool
    can_manage_voice_chats : bool
    can_restrict_members : bool
    can_promote_members : bool
    can_change_info : bool
    can_invite_users : bool
    can_post_messages : bool
    can_edit_messages : bool
    can_pin_messages : bool
    can_manage_topics : bool
    def __init__(self,**kwargs):
        self.is_anonymous = kwargs.get('is_anonymous', False)
        self.can_manage_chat = kwargs.get('can_manage_chat', False)
        self.can_delete_messages = kwargs.get('can_delete_messages', False)
        self.can_manage_voice_chats = kwargs.get('can_manage_voice_chats', False)
        self.can_restrict_members = kwargs.get('can_restrict_members', False)
        self.can_promote_members = kwargs.get('can_promote_members', False)
        self.can_change_info = kwargs.get('can_change_info', False)
        self.can_invite_users = kwargs.get('can_invite_users', False)
        self.can_post_messages = kwargs.get('can_post_messages', False)
        self.can_edit_messages = kwargs.get('can_edit_messages', False)
        self.can_pin_messages = kwargs.get('can_pin_messages', False)
        self.can_manage_topics = kwargs.get('can_manage_topics', False)