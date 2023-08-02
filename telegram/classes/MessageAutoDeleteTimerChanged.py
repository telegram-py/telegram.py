class MessageAutoDeleteTimerChanged:
    message_auto_delete_time : int
    def __init__(self,**kwargs):
        self.message_auto_delete_time = kwargs.get('message_auto_delete_time')
        