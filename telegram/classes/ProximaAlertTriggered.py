class ProximaAlertTriggered:
    traveller : User
    watcher : User
    distance : int
    def __init__(self,**kwargs):
        self.traveller = User(**kwargs.get('traveller'))
        self.watcher = User(**kwargs.get('watcher'))
        self.distance = kwargs.get('distance')

