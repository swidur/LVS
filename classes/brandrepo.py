from brand import Brand
from connector import Connector


class BrandRepo:
    def __init__(self):
        self.connection = Connector.connect()

    @staticmethod
    def create_brand(brand):
        return Brand(brand[0], brand[1])

    def select_one(self, b_id):
        db = self.connection
        c = db.cursor()
        c.execute('select * from Brands where id={};'.format(b_id))
        brand = c.fetchone()
        return self.create_brand(brand)

    def select_all(self):
        db = self.connection
        c = db.cursor()
        c.execute('select * from Brands;')
        brands = []
        for brand in c.fetchall():
            brands.append(BrandRepo.create_brand(brand))
        return brands