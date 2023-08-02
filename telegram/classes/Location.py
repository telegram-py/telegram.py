class Location:
    longitude: float
    latitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int

    def __init__(self, **kwargs):
        self.longitude = kwargs.get('longitude')
        self.latitude = kwargs.get('latitude')
        self.horizontal_accuracy = kwargs.get('horizontal_accuracy')
        self.live_period = kwargs.get('live_period')
        self.heading = kwargs.get('heading')
        self.proximity_alert_radius = kwargs.get('proximity_alert_radius')
    
    