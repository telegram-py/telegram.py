from telegram.classes.User import User
from telegram.classes.Location import Location

class InlineQuery:
    id : str
    from_user : User
    query : str
    offset : str
    chat_type : str
    location : Location
    def __init__(self,**kwargs):
        self.id = kwargs.get('id')
        self.from_user = User(**kwargs.get('from'))
        self.query = kwargs.get('query')
        self.offset = kwargs.get('offset')
        self.chat_type = kwargs.get('chat_type')
        self.location = Location(**kwargs.get('location')) if kwargs.get('location') else None
