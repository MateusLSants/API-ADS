from flask.json import JSONEncoder

class Users(object):
    new_id = 1

    def __init__(self, name) -> None:
        self.name
        self.id = Users.new_id
        Users.new_id += 1