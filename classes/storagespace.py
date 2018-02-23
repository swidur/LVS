class StorageSpace:
    def __init__(self, stillage, x, y):
        self.y = y
        self.x = x
        self.stillage = stillage

    def address(self):
        address = [self.stillage, self.x, self.y]
        return address

    def __repr__(self):
        return 'repr: StorageSpace({},{},{})'.format(self.stillage, self.x, self.y)

    def __str__(self):
        return 'str: Stillage: {}, x: {}, y: {}'.format(self.stillage, self.x, self.y)
