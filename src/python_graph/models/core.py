from python_graph.db.connection import DBConnection


class CustomContext:

    def __init__(self, db: DBConnection):
        self.db = db
