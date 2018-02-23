class TreadType:
    def __init__(self, type_id, name):
        self.type_id = type_id
        self.name = name

    def __repr__(self):
        return 'repr: Tread({},{})'.format(self.type_id, self.name)

    def __str__(self):
        return 'str: Tread: ID: {} NAME: {}'.format(self.type_id, self.name)
