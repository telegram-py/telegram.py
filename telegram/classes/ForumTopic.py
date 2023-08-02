class ForumTopic:
    message_thread_id : int
    name : str
    icon_color : int
    icon_custom_emoji : str
    def __init__(self,**kwargs):
        self.message_thread_id = kwargs.get('message_thread_id', 0)
        self.name = kwargs.get('name', "")
        self.icon_color = kwargs.get('icon_color', 0)
        self.icon_custom_emoji = kwargs.get('icon_custom_emoji', "")