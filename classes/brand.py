class Brand:
    def __init__(self, b_id, name):
        self.b_id = b_id
        self.name = name

    def __repr__(self):
        return 'repr: Brand({},{})'.format(self.b_id, self.name)

    def __str__(self):
        return 'str: Brand: ID:{} NAME:{}'.format(self.b_id, self.name)