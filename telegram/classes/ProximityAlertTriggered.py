from telegram.classes.User import User


class ProximityAlertTriggered:
    traveler: User
    watcher: User
    distance: int

    def __init__(self, **kwargs):
        self.traveler = User(**kwargs.get('traveler'))
        self.watcher = User(**kwargs.get('watcher'))
        self.distance = kwargs.get('distance', 0)
