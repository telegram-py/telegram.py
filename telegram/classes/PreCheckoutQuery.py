from telegram.classes.User import User
from telegram.classes.OrderInfo import OrderInfo
class PreCheckoutQuery:
    id : str
    from_user : User
    currency : str
    total_amount : int
    invoice_payload : str
    shipping_option_id : str
    order_info : OrderInfo
    def __init__(self,**kwargs):
        self.id = kwargs.get('id')
        self.from_user = User(**kwargs.get('from'))
        self.currency = kwargs.get('currency')
        self.total_amount = kwargs.get('total_amount')
        self.invoice_payload = kwargs.get('invoice_payload')
        self.shipping_option_id = kwargs.get('shipping_option_id',None)
        self.order_info = OrderInfo(**kwargs.get('order_info')) if kwargs.get('order_info') else None