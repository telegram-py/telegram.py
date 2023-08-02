class ForceReply:
    force_reply : bool
    input_field_placeholder : str
    selective : bool
    def __init__(self,**kwargs):
        self.force_reply = kwargs.get('force_reply', False)
        self.input_field_placeholder = kwargs.get('input_field_placeholder', "")
        self.selective = kwargs.get('selective', False)