
class StorageSpace:
    def __init__(self, stillage, x, y):
        self.y = y
        self.x = x
        self.stillage = stillage

    def address(self):
        address = [self.stillage, self.x, self.y]
        return address

