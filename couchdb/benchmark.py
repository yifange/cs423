import string
import random
import time

from couchdbkit import *
from couchdbkit.designer import push

class Benchmark(Document):

    key = StringProperty()
    content = StringProperty()


def string_generator(size):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def regular_insert(db, count, size):
    a = []
    for i in range(0, count):
        a.append(Benchmark(key=str(i), content=string_generator(size)))
    start_time = time.time()
    for item in a:
        print item.content
        db.save_doc(item)
    end_time = time.time()
    print "Time used: ", end_time - start_time

def bulk_insert(db, count, size):
    a = []
    for i in range(0, count):
       a.append(Benchmark(key=str(i), content=string_generator(size)))
    start_time = time.time()
    db.bulk_save(a)
    end_time = time.time()
    print "Time used: ", end_time - start_time


def get_all(db):
    start_time = time.time()
    docs = Benchmark.view("benchmark/all")
    # print docs.all()
    end_time = time.time()
    print "Time used: ", end_time - start_time


def random_read(db, key_range, count):
    start_time = time.time()
    for i in range(0, count):
        rand_key = str(random.randrange(0, key_range))
        docs = Benchmark.view("benchmark/all", key=rand_key)
        # print docs.first()

    end_time = time.time()
    print "Time used: ", end_time - start_time

def range_read(db, key_range, fraction):
    start_time = time.time()
    if fraction == 1:
        start_key = 0
        fraction_range = int(key_range)
    else:
        fraction_range = int(key_range * fraction)
        start_key = random.randrange(0, key_range - fraction_range)
    docs = Benchmark.view("benchmark/all", start_key=str(start_key), end_key=str(start_key + fraction_range))
    end_time = time.time()
    print "Time used: ", end_time - start_time

def stupid_range_read(db, key_range, fraction):
    start_time = time.time()
    if fraction == 1:
        start_key = 0
        fraction_range = int(key_range)
    else:
        fraction_range = int(key_range * fraction)
        start_key = random.randrange(0, key_range - fraction_range)
    for key in range(start_key, start_key + key_range):
        doc = Benchmark.view("benchmark/all", key=str(key))
    end_time = time.time()
    print "Time used: ", end_time - start_time
if __name__ == "__main__":
    server = Server()

    db = server.get_or_create_db("benchmark")
    # push("_design/benchmark", db)
    db.flush()
    # Benchmark.set_db(db)
    # regular_insert(db, 1, 16000)
    # bulk_insert(db, 1000, 10)
    # get_all(db)
    # random_read(db, 100000, 10000)

    # range_read(db, 100000, 1)
    # stupid_range_read(db, 100000, 0.125)
