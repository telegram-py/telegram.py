from telegram.classes.PassportFile import PassportFile


class EncryptedPassportElement:
    type: str
    data: str
    phone_number: str
    email: str
    files: list[PassportFile]
    front_side: PassportFile
    reverse_side: PassportFile
    selfie: PassportFile
    translation: list[PassportFile]
    hash: str

    def __init__(self, **kwargs):
        self.type = kwargs.get('type', '')
        self.data = kwargs.get('data', '')
        self.phone_number = kwargs.get('phone_number', '')
        self.email = kwargs.get('email', '')
        self.files = [PassportFile(**s) for s in kwargs.get('files', [])]
        self.front_side = PassportFile(**kwargs.get('front_side', {}))
        self.reverse_side = PassportFile(**kwargs.get('reverse_side', {}))
        self.selfie = PassportFile(**kwargs.get('selfie', {}))
        self.translation = [PassportFile(**s) for s in kwargs.get('translation', [])]
        self.hash = kwargs.get('hash', '')
