class ChatLocation:
    location : Location
    address : str
    def __init__(self,**kwargs):
        self.location = Location(**kwargs.get('location', dict()))
        self.address = kwargs.get('address', "")