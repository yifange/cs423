import datetime

from couchdbkit import *


class Greeting(Document):
    author = StringProperty()
    content = StringProperty()
    date = DateTimeProperty()

if __name__ == "__main__":
    server = Server()

    db = server.get_or_create_db("greeting")

    Greeting.set_db(db)

    greet = Greeting(author="benoit",
                     content="Welcome to couchdbkit world",
                     date=datetime.datetime.utcnow()
                     )
    greet.save()
