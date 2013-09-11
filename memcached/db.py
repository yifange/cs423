import MySQLdb
import string
import random


class Db(object):

    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root',
                                    'cs423', 'cs423_restful')
        self.cursor = self.conn.cursor()

    def clean(self):
        sql = "TRUNCATE test"
        self.cursor.execute(sql)

    def get(self, key):
        sql = "SELECT name, value FROM test WHERE name='%s'" % key
        self.cursor.execute(sql)
        numrows = int(self.cursor.rowcount)
        if numrows:
            row = self.cursor.fetchone()
            print row[0], "-->", row[1]

    def put(self, key, value):
        sql = "INSERT INTO test (name, value) VALUES ('%s', '%s')" \
            % (key, value)
        print sql
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLdb.Error as e:
            print e
            return False
        return True

    def string_generator(self, size):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for x in range(size))

    def random_insert(self):
        self.clean()
        for num in range(1000):
            name = "KEY_" + str(num)
            value = self.string_generator(300)
            self.put(name, value)

    def random_read(self):
        for i in range(100):
            name = "KEY_" + str(random.randrange(0, 1000))
            self.get(name)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = Db()
    # db.random_insert()
    db.random_read()
