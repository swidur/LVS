import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname='lvs' user='postgres' host='localhost' password='Hyd2Oxyg2'")

