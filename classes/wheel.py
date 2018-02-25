class Wheel:
    def __init__(self, w_id, width, height, inches, t_depth, t_type, brand, dot, storage_space, aggregate):
        self.w_id = w_id
        self.dot = dot
        self.t_type = t_type
        self.t_depth = t_depth
        self.inches = inches
        self.height = height
        self.width = width
        self.brand = brand
        self.storage_space = storage_space
        self.aggregate = aggregate

    def gen_size(self):
        w_size = "{}/{}/{}'".format(self.width, self.height, self.inches)
        return w_size

    def all_info(self):
        return [self.w_id, self.width, self.height, self.inches, self.t_depth, self.t_type, self.brand, self.dot, self.storage_space, self.aggregate]

    def __repr__(self):
        return 'repr: Wheel({},{},{},{},{},{},{},{})'.format(self.w_id, self.width, self.height, self.inches, self.t_depth,
                                                       self.t_type, self.brand, self.dot, self.storage_space,
                                                       )

    def __str__(self):
        return 'str: ID:{} {}, {}'.format(self.w_id, self.gen_size(), self.brand)