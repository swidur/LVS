import sqlite3 as lite


class Connector:
    def __init__(self, path='default.db'):
        self.path = path
        self.default = 'default.db'

    def connect(self):
        """Connect to the SQLite database. Returns a database connection."""

        try:
            return lite.connect(self.path)

        except lite.OperationalError:
            return lite.connect(self.default)