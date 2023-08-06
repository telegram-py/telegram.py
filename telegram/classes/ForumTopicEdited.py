class ForumTopicEdited:
    topic: str
    icon_custom_emoji_id: str

    def __init__(self, **kwargs):
        self.topic = kwargs.get('topic')
        self.icon_custom_emoji_id = kwargs.get('icon_custom_emoji_id')
