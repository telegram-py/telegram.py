class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str
    is_premium: bool
    added_to_attachment_menu: bool
    can_join_groups: bool
    can_read_all_group_messages: bool
    supports_inline_queries: bool

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.is_bot = kwargs.get('is_bot')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.username = kwargs.get('username')
        self.language_code = kwargs.get('language_code')
        self.is_premium = kwargs.get('is_premium')
        self.added_to_attachment_menu = kwargs.get('added_to_attachment_menu')
        self.can_join_groups = kwargs.get('can_join_groups')
        self.can_read_all_group_messages = kwargs.get('can_read_all_group_messages')
        self.supports_inline_queries = kwargs.get('supports_inline_queries')
