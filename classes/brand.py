class Brand:
    def __init__(self, b_id, name):
        self.b_id = b_id
        self.name = name

    def __repr__(self):
        return 'Brand({},{})'.format(self.b_id, self.name)

    def __str__(self):
        # return 'ID:{} {}/{}/{}, {}'.format(self.w_id, self.width, self.height, self.inches, self.brand)
        return 'Brand: ID:{} NAME:{}'.format(self.b_id, self.name)