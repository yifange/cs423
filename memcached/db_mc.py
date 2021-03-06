import MySQLdb
import pylibmc
import string
import random
import time


class Db(object):

    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root',
                                    'cs423', 'cs423_restful')
        self.cursor = self.conn.cursor()
        self.mc = pylibmc.Client(['127.0.0.1'],
                                 binary=True,
                                 behaviors={'tcp_nodelay': True,
                                            'ketama': True})

    def clean(self):
        sql = "TRUNCATE test"
        self.cursor.execute(sql)

    def flush_memcache(self):
        self.mc.flush_all()

    def get(self, key):
        if key in self.mc:
            return key + "-->" + self.mc[key]
        else:
            sql = "SELECT name, value FROM test WHERE name='%s'" % key
            self.cursor.execute(sql)
            numrows = int(self.cursor.rowcount)
            if numrows:
                row = self.cursor.fetchone()
                self.mc[key] = row[1]
                return row[0] + "-->" + row[1]
            else:
                return None

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
            r = self.get(name)
            # print r if r else ""

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = Db()
    # db.flush_memcache()
    start_time = time.time()
    db.random_read()
    end_time = time.time()
    print "Time used: ", end_time - start_time
