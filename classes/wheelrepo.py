from brandrepo import BrandRepo
from connector import Connector
from wheel import Wheel


class WheelRepo:
    def __init__(self):
        self.connection = Connector.connect()

    @staticmethod
    def create_wheel(wheel):
        return Wheel(wheel[0], wheel[1], wheel[2], wheel[3], wheel[4], wheel[5], BrandRepo().select_one(wheel[6]).name,
                     wheel[7], wheel[8])

    def select_one(self, w_id):
        db = self.connection
        c = db.cursor()
        c.execute('select * from Wheel where id={};'.format(w_id))
        wheel = c.fetchone()
        return self.create_wheel(wheel)

    def delete(self, w_id):
        if isinstance(w_id, Wheel):
            w_id = w_id.w_id
        db = self.connection
        c = db.cursor()
        c.execute('delete from Wheel where id={}; commit;'.format(w_id))

    def delete_via_instance(self, wheel):
        db = self.connection
        c = db.cursor()
        c.execute('delete from Wheel where id={};'.format(wheel.w_id))

    def select_all(self):
        db = self.connection
        c = db.cursor()
        c.execute('select * from Wheel;')
        wheels = []
        for wheel in c.fetchall():
            wheels.append(WheelRepo.create_wheel(wheel))
        return wheels
