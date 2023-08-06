class ChatPermissions:
    can_send_messages: bool
    can_send_audios: bool
    can_send_documents: bool
    can_send_photos: bool
    can_send_videos: bool
    can_send_video_notes: bool
    can_send_voice_notes: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool

    def __init__(self, **kwargs):
        self.can_send_messages = kwargs.get('can_send_messages', False)
        self.can_send_audios = kwargs.get('can_send_audios', False)
        self.can_send_documents = kwargs.get('can_send_documents', False)
        self.can_send_photos = kwargs.get('can_send_photos', False)
        self.can_send_videos = kwargs.get('can_send_videos', False)
        self.can_send_video_notes = kwargs.get('can_send_video_notes', False)
        self.can_send_voice_notes = kwargs.get('can_send_voice_notes', False)
        self.can_send_polls = kwargs.get('can_send_polls', False)
        self.can_send_other_messages = kwargs.get('can_send_other_messages', False)
        self.can_add_web_page_previews = kwargs.get('can_add_web_page_previews', False)
        self.can_change_info = kwargs.get('can_change_info', False)
        self.can_invite_users = kwargs.get('can_invite_users', False)
        self.can_pin_messages = kwargs.get('can_pin_messages', False)
        self.can_manage_topics = kwargs.get('can_manage_topics', False)
