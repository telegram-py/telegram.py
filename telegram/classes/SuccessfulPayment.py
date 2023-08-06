from telegram.classes.OrderInfo import OrderInfo


class SuccessfulPayment:
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: OrderInfo
    telegram_payment_charge_id: str
    provider_payment_charge_id: str

    def __init__(self, **kwargs):
        self.currency = kwargs.get('currency', '')
        self.total_amount = kwargs.get('total_amount', 0)
        self.invoice_payload = kwargs.get('invoice_payload', '')
        self.shipping_option_id = kwargs.get('shipping_option_id', '')
        self.order_info = OrderInfo(**kwargs.get('order_info', {}))
        self.telegram_payment_charge_id = kwargs.get('telegram_payment_charge_id', '')
        self.provider_payment_charge_id = kwargs.get('provider_payment_charge_id', '')
