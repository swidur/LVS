from brandrepo import BrandRepo
from tread_typerepo import TreadTypeRepo
from connector import Connector
from wheel import Wheel


class WheelRepo:
    def __init__(self):
        self.connection = Connector().connect()

    @staticmethod
    def create_wheel(wheel):
        return Wheel(wheel[0], wheel[1], wheel[2], wheel[3], wheel[4], TreadTypeRepo().select_one(wheel[5]).name,
                     BrandRepo().select_one(wheel[6]).name,
                     wheel[7], wheel[8], wheel[9])

    def delete_via_id(self, w_id):
        if isinstance(w_id, Wheel):
            w_id = w_id.w_id
        db = self.connection
        c = db.cursor()
        c.execute('delete from Wheel where id={}; commit;'.format(w_id))

    def delete_via_instance(self, wheel):
        db = self.connection
        c = db.cursor()
        c.execute('delete from Wheel where id={};'.format(wheel.w_id))

    def select_one(self, w_id):
        db = self.connection
        c = db.cursor()
        c.execute('select * from wheel where wheel_id={};'.format(w_id))
        wheel = c.fetchone()

        return self.create_wheel(wheel)

    def select_all(self):
        db = self.connection
        c = db.cursor()
        c.execute('select * from Wheel order by inches, width;')
        wheels = []
        for wheel in c.fetchall():
            wheels.append(WheelRepo.create_wheel(wheel))
        return wheels

    def add_new(self, wheel):
        # create new wheel out of wheel object and add it to the database
        db = self.connection
        c = db.cursor()
        if isinstance(wheel, Wheel):
            c.execute("INSERT INTO wheel VALUES ({},{},{},{},{},{},{},{},{},{});".format(wheel.w_id, wheel.width,
                                                                                         wheel.height, wheel.inches,
                                                                                         wheel.t_depth, wheel.t_type,
                                                                                         wheel.brand, wheel.dot,
                                                                                         wheel.storage_space,
                                                                                         wheel.aggregate))
            db.commit()
        else:
            raise TypeError('Not a Wheel object')
