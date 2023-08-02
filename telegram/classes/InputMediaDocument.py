class InputMediaDocument:
    type : str
    media : str
    thumb : InputFile
    caption : str
    parse_mode : str
    caption_entities : list[MessageEntity]
    disable_content_type_detection : bool
    def __init__(self, **kwargs):
        self.type = 'document'
        self.media = str(kwargs.get('media', ''))
        self.thumb = InputFile(**kwargs.get('thumb', {}))
        self.caption = str(kwargs.get('caption', ''))
        self.parse_mode = str(kwargs.get('parse_mode', ''))
        self.caption_entities =[ MessageEntity(**x) for x in kwargs.get('caption_entities', []) ]
        self.disable_content_type_detection = bool(kwargs.get('disable_content_type_detection', False))