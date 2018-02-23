from connector import Connector
from storagespace import StorageSpace


class StorageRepo:
    def __init__(self):
        self.connection = Connector().connect()

    @staticmethod
    def create_StorageSpace(storage_space):
        return StorageSpace(storage_space[0], storage_space[1], storage_space[2])

    def select_all(self):
        # returns a list of StorageSpace instances from database
        db = self.connection
        c = db.cursor()
        c.execute('select * from storagespaces order by storage_id;')
        spaces = []
        for storage_space in c.fetchall():
            spaces.append(StorageRepo().create_StorageSpace(storage_space))
        return spaces

    def get_address(self, wheel):
        # returns address of wheel instance as a list: [storage_id, stillage, x, y]
        db = self.connection
        c = db.cursor()
        c.execute('select * from storagespaces where storage_id={};'.format(wheel.storage_space))
        self.storage = c.fetchone()
        c.close()
        return [self.storage[0], self.storage[1], self.storage[2], self.storage[3]]

    def get_address_verbose(self, wheel):
        # returns  address of wheel instance as a string: "ID: storage_id, stillage: stillage, X:x, Y:y"
        self.get_address(wheel)
        return "ID: {}, stillage: {}, X:{}, Y:{}".format(self.storage[0], self.storage[1], self.storage[2],
                                                         self.storage[3])

    def new_space_from_instance(self, storagespace):
        # adds new storage space to database. Takes StorageSpace instance as an arg
        db = self.connection
        c = db.cursor()
        c.execute("insert into storagespaces values(NULL, '{}',{},{})".format(storagespace.stillage, storagespace.x,
                                                                              storagespace.y))
        db.commit()
