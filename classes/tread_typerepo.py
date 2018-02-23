from connector import Connector
from tread_type import TreadType


class TreadTypeRepo:
    def __init__(self):
        self.connection = Connector().connect()

    @staticmethod
    def create_TreadType(tread_type):
        # returns object od TreadType class
        return TreadType(tread_type[0], tread_type[1])

    def select_one(self, type_id):
        db = self.connection
        c = db.cursor()
        c.execute('select * from t_types where type_id={};'.format(type_id))
        tread_type = c.fetchone()

        return self.create_TreadType(tread_type)

    def select_all(self):
        # return list of TreadType instances of all types of tread in db
        db = self.connection
        c = db.cursor()
        c.execute('select * from t_types order by type_id;')
        treads = []
        for tread_type in c.fetchall():
            treads.append(TreadTypeRepo.create_TreadType(tread_type))
        return treads
