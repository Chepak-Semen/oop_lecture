"""Create two classes: Laptop, Guitare, one for composition, another one for aggregation."""


class Laptop:
    def __init__(self):
        self.os = Os()


class Os:
    def __init__(self):
        self.type = 'Windows'
        self.version = 'Xp'
        self.updates = False
