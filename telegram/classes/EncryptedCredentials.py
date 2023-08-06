class EncryptedCredentials:
    data: str
    hash: str
    secret: str

    def __init__(self, **kwargs):
        self.data = kwargs.get('data')
        self.hash = kwargs.get('hash')
        self.secret = kwargs.get('secret')
