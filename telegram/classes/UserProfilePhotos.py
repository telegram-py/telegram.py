from telegram.classes.PhotoSize import PhotoSize


class UserProfilePhotos:
    total_count: int
    photos: list[list[PhotoSize]]

    def __init__(self, **kwargs):
        self.total_count = kwargs.get('total_count', 0)
        self.photos = [list[PhotoSize](s) for s in kwargs.get('photos', [])]
