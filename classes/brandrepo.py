from brand import Brand
from connector import Connector


class BrandRepo:
    def __init__(self):
        self.connection = Connector().connect()

    @staticmethod
    def create_brand(brand):
        return Brand(brand[0], brand[1])

    def select_one(self, b_id):
        # select brand from database by id, return brand object
        db = self.connection
        c = db.cursor()
        c.execute('SELECT * FROM brands WHERE brand_id = {};'.format(b_id))
        brand = c.fetchone()
        return self.create_brand(brand)

    def select_all(self):
        # select all brands from database, return list of brand objects
        db = self.connection
        c = db.cursor()
        c.execute('SELECT * FROM brand;')
        brands = []
        for brand in c.fetchall():
            brands.append(BrandRepo.create_brand(brand))
        return brands

    def add_new(self, brand):
        # create new brand out of brand object and add it to the database
        db = self.connection
        c = db.cursor()
        if isinstance(brand, Brand):
            c.execute("INSERT INTO brand values ({},'{}');".format(brand.b_id, brand.name))
            db.commit()
        else:
            raise TypeError('Not a Brand object')
