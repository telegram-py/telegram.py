class MyContact:
    phone_number: str
    first_name: str
    last_name: str
    user_id: int
    vcard: str
    
    def __init__(self, **kwargs):
        self.phone_number = kwargs.get('phone_number')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.user_id = kwargs.get('user_id')
        self.vcard = kwargs.get('vcard')