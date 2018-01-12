import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname='lvm' user='postgres' host='localhost' password='Hyd2Oxyg2'")


def read_db(id):
    db = connect()
    c = db.cursor()
    c.execute('select * from Wheel where id={};'.format(id))
    wheel = c.fetchone()
    id, width, height, inches, t_depth, t_type, brand, dot, storage_space = wheel[0], wheel[1], wheel[2], wheel[3], wheel[4], wheel[5], wheel[6], wheel[7], wheel[8]
    # for i in c.fetchone():
    #     print i
    print width,height,inches

print read_db(4)
