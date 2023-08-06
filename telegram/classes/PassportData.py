from telegram.classes.EncryptedPassportElement import EncryptedPassportElement
from telegram.classes.EncryptedCredentials import EncryptedCredentials


class PassportData:
    data: list[EncryptedPassportElement]
    credentials: EncryptedCredentials

    def __init__(self, **kwargs):
        self.data = [EncryptedPassportElement(**s) for s in kwargs.get('data', [])]
        self.credentials = EncryptedCredentials(**kwargs.get('credentials', {}))
