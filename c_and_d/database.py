import psycopg2

# TODO: implement methods for pulling column data from information_schema.columns
#       SELECT table_name, column_name, data_type, column_default, is_nullable, character_maximum_length FROM information_schema.columns;
#       --https://www.postgresqltutorial.com/postgresql-describe-table/
#       --https://www.postgresql.org/docs/13/infoschema-columns.html
# TODO: A thought - Module should be written in a manner that assumes little to no knowledge of db, that responsiblity belongs in main.

# This code has not been tested, presume broken
# NEXT: Write out methods, class structure as if 'in a black box'.
#       Implement methods, and write tests.


class Database:
    """Handles connection to database"""

    def __init__(self, dbname, password, host='localhost', user='postgres', ):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password

    def __connect__(self):
        try:
            self.conn = psycopg2.connect("dbname=self.dbname user=self.user \
            host=self.host password=self.password")
            self.cur = self.con.cursor()
        except:
            print("Connection failed")

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()

        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()