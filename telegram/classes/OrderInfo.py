from telegram.classes.ShippingAddress import ShippingAddress


class OrderInfo:
    name: str
    phone_number: str
    email: str
    shipping_address: ShippingAddress

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.phone_number = kwargs.get('phone_number', '')
        self.email = kwargs.get('email', '')
        self.shipping_address = ShippingAddress(**kwargs.get('shipping_address', {}))
