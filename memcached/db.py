import MySQLdb
import string
import random

def clean(cursor):
    sql = "TRUNCATE test"
    cursor.execute(sql)

def get(cursor, key):
    sql = "SELECT name, value FROM test WHERE name='%s'" % key
    cursor.execute(sql)
    numrows = int(cursor.rowcount)
    for x in range(numrows):
        row = cursor.fetchone()
        print row[0], "-->", row[1]

def put(conn, cursor, key, value):
    sql = "INSERT INTO test (name, value) VALUES ('%s', '%s')" % (key, value)
    try:
        cursor.execute(sql)
        conn.commit()
    except MySQLdb.Error as e:
        print e
        return False
    return True


def string_generator(size):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def random_insert(conn, cursor):
    clean(cursor)
    for num in range(1000):
        name = "KEY_" + str(num)
        value = string_generator(300)
        put(conn, cursor, name, value)

def random_read(cursor):
    for i in range(100):
        name = "KEY_" + str(random.randrange(0, 1000))
        get(cursor, name)

if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', user='root', passwd='cs423', db='cs423_restful')
    cursor = conn.cursor()
    # random_insert(conn, cursor)
    random_read(cursor)
    cursor.close()
    conn.close()
