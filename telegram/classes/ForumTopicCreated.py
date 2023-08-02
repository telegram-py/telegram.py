class ForumTopicCreated:
    name : str
    icon_color : str
    icon_custom_emoji_id : str
    
    def __init__(self,**kwargs):
        self.name = kwargs.get('name')
        self.icon_color = kwargs.get('icon_color')
        self.icon_custom_emoji_id = kwargs.get('icon_custom_emoji_id')
