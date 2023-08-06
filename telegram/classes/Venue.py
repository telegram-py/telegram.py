from telegram.classes.Location import Location


class Venue:
    location: Location
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str

    def __init__(self, **kwargs):
        self.location = Location(**kwargs.get('location'))
        self.title = kwargs.get('title')
        self.address = kwargs.get('address')
        self.foursquare_id = kwargs.get('foursquare_id')
        self.foursquare_type = kwargs.get('foursquare_type')
        self.google_place_id = kwargs.get('google_place_id')
        self.google_place_type = kwargs.get('google_place_type')
