from telegram.classes.User import User
from telegram.classes.Location import Location

class ChosenInlineResult:
    result_id : str
    from_user : User
    location : Location
    inline_message_id : str
    query : str
    def __init__(self,**kwargs):
        self.result_id = kwargs.get('result_id')
        self.from_user = User(**kwargs.get('from'))
        self.location = Location(**kwargs.get('location')) if kwargs.get('location') else None
        self.inline_message_id = kwargs.get('inline_message_id',None)
        self.query = kwargs.get('query')