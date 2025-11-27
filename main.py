import json
import sqlite3
import strawberry
import typing

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker


engine = sa.create_engine("sqlite:///graphql_sqlite.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)


ACTIONS = {
    "1": "insert",
    "2": "consult",
}
INSERT_ACTIONS = {
    "books": "addBook",
    "persons": "addPerson",
}
MODELS = {
    "1": "books",
    "2": "persons",
}
BOOKS_FIELDNAMES_2 = [
    ("id", int),
    ("title", str),
    ("author", str)
]
PERSONS_FIELDNAMES_2 = [
    ("id", int),
    ("name", str),
    ("age", int),
    ("height", float),
    ("isStudent", bool)
]


def _check_is_string(value: str):
    return True, f'"{value}"'


def _check_is_int(value: str):
    if not value.isdigit():
        return False, None
    return True, int(value)


def _check_is_float(value: str):
    if not value.replace('.', '', 1).isdigit():
        return False, None
    return True, float(value)


def _check_is_bool(value: str):
    lowered = value.lower()
    if lowered in ["true", "1", "yes"]:
        return True, "true"
    elif lowered in ["false", "0", "no"]:
        return True, "false"
    else:
        return False, None


VALIDATORS = {
    str: _check_is_string,
    int: _check_is_int,
    float: _check_is_float,
    bool: _check_is_bool
}


def create_tables():
    with sqlite3.connect("graphql_sqlite.db") as connection:
        with open("database.sql", "r") as f:
            connection.executescript(f.read())
        connection.commit()


def check_table_creation():
    with sqlite3.connect("graphql_sqlite.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(table[0])


@strawberry.type
class Book:
    id: int
    title: str
    author: str


@strawberry.type
class Person:
    id: int
    name: str
    age: int
    height: float
    is_student: bool


@strawberry.type
class BookQuery:

    @strawberry.field
    def books(self) -> typing.List[Book]:
        with Session() as session:
            print("Fetching books from database...")
            result = session.execute(sa.text("SELECT id, title, author FROM books")).mappings().all()
            books = [Book(id=row["id"], title=row["title"], author=row["author"]) for row in result]
            return books


@strawberry.type
class BookMutation:

    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        with Session() as session:
            session.execute(
                sa.text("INSERT INTO books (title, author) VALUES (:title, :author)"),
                {"title": title, "author": author},
            )
            result = session.execute(sa.text("SELECT last_insert_rowid()")).scalar_one()
            session.commit()
            return Book(id=result, title=title, author=author)


@strawberry.type
class PersonMutation:

    @strawberry.mutation
    def add_person(self, name: str, age: int, height: float, is_student: bool) -> Person:
        with Session() as session:
            session.execute(
                sa.text("INSERT INTO persons (name, age, height, is_student) VALUES (:name, :age, :height, :is_student)"),
                {"name": name, "age": age, "height": height, "is_student": int(is_student)},
            )
            result = session.execute(
                sa.text("SELECT last_insert_rowid()")).scalar_one()
            session.commit()
            return Person(
                id=result, name=name,
                age=age, height=height,
                is_student=is_student)


@strawberry.type
class PersonQuery:

    @strawberry.field
    def persons(self) -> typing.List[Person]:
        with Session() as session:
            print("Fetching persons from database...")
            result = session.execute(
                sa.text(
                    "SELECT id, name, age, height, is_student FROM persons"
                )
            ).mappings().all()
            persons = [
                Person(
                    id=row["id"],
                    name=row["name"],
                    age=row["age"],
                    height=row["height"],
                    is_student=bool(row["is_student"]),
                )
                for row in result
            ]
            return persons


@strawberry.type
class Query(BookQuery, PersonQuery):
    pass


@strawberry.type
class Mutation(BookMutation, PersonMutation):
    pass


MODELS_TEXT = """
1. Books
2. Persons
"""


def _ask_working_model():
    model = input(f"""Which model do you want to work with?:
{MODELS_TEXT}Select: """).strip().lower()
    return _get_model_class(model)


def _get_model_class(model_name: str):
    return MODELS.get(model_name)


def _ask_fieldnames(fields: list[str]):
    fields_selected = input(f"""Which fields do you want to work with?
{fields}
(separate by comma, leave empty for all): """).strip().lower().split(",")
    if len(fields_selected) == 1 and fields_selected[0] == "all":
        return fields

    return fields_selected


def _get_fieldnames(model_name: str):
    return globals().get(f"{model_name.upper()}_FIELDNAMES_2")


def consult(schema):
    model = _ask_working_model()
    fields_types = _get_fieldnames(model)
    fields = [field for field, _ in fields_types]
    fields_asked = _ask_fieldnames(fields)
    query_2 = f"query {{ {model} {{ {', '.join(fields_asked)} }} }}"
    return schema.execute_sync(query_2)


def _ask_insertion_data(fieldnames: list[tuple[str, type]]):
    fields = [field for field, _ in fieldnames]

    print("Provide the following data:", fields)
    data = {}
    for field, type_field in fieldnames:
        while True:
            value = input(f"{field}: ").strip()
            result_validator, parsed_value = VALIDATORS.get(type_field)(value)
            if result_validator:
                data[field] = parsed_value
                break
            else:
                print(
                    f"Invalid value for field {field}. "
                    f"Expected type: {type_field.__name__}")

    return data


def insert(schema):
    model = _ask_working_model()
    fields = _get_fieldnames(model)
    fieldnames = [field for field, _ in fields]

    data = _ask_insertion_data([(x, _) for x, _ in fields if x != "id"])
    print("Inserting data:", data)
    mutation = f"""
    mutation {{
        {INSERT_ACTIONS[model]}({', '.join([
            f'{key}: {value}' for key, value in data.items()])}) {{
            {', '.join(fieldnames)}
        }}
    }}
"""
    return schema.execute_sync(mutation)


def main():
    # create_tables()
    # check_table_creation()

    action = input("""What do you want to do?:
1. Insert
2. Consult
Select: """).strip().lower()

    if action not in ACTIONS:
        print("Invalid action.")
        exit()

    schema = strawberry.Schema(query=Query, mutation=Mutation)
    result = globals()[ACTIONS[action]](schema)
    print(json.dumps(result.data, indent=4))


if __name__ == "__main__":
    main()
