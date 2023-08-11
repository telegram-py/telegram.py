from telegram.classes.User import User
from telegram.classes.ShippingAddress import ShippingAddress
class ShippingQuery:
    id : str
    from_user : User
    invoice_payload : str
    shipping_address : ShippingAddress
    def __init__(self,**kwargs):
        self.id = kwargs.get('id')
        self.from_user = User(**kwargs.get('from'))
        self.invoice_payload = kwargs.get('invoice_payload')
        self.shipping_address = ShippingAddress(**kwargs.get('shipping_address'))