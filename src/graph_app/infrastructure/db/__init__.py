from functools import wraps
import json


def get_init_structure():
    return {
        "teams": {
            "records": [],
        },
    }


def update_db(content: dict, path: str = 'db.json'):
    with open(path, 'w+', encoding='utf-8') as file:
        file.write(json.dumps(content, indent=4))


def load_db(path: str = 'db.json'):
    database_json = get_init_structure()
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            database_json = json.loads(content)
    except json.decoder.JSONDecodeError:
        update_db(database_json)

    return database_json


def read_cache_database(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        database = load_db()
        return func(database=database, *args, **kwargs)

    return wrapper_func


class MathDBOpteration():

    table: str
    database: dict

    def _get_records(self):
        return self.database[self.table]['records']

    def get_max_id(self):
        records = self._get_records()
        return records and max(record['id'] for record in records) or 0

    def filter_by_field(self, field, value):
        records = self._get_records()
        record = [record for record in records if record[field] == value]
        if record:
            return record[0]

        return None

    def add_record(self, record):
        self.database[self.table]['records'].append(record)
    
    def get_all_records(self):
        return self.database[self.table]['records']


def connection_db(_class):

    class DBClass(_class, MathDBOpteration):

        def __init__(self) -> None:
            super().__init__()
            self.database = load_db()

        def update_db(self) -> bool:
            update_db(self.database)
            return True
    return DBClass
