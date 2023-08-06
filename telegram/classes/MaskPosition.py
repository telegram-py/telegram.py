class MaskPosition:
    point: str
    x_shift: float
    y_shift: float
    scale: float

    def __init__(self, **kwargs):
        self.point = kwargs.get('point', "")
        self.x_shift = kwargs.get('x_shift', 0)
        self.y_shift = kwargs.get('y_shift', 0)
        self.scale = kwargs.get('scale', 0)
