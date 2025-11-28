import json
import sys

import sqlite3
import strawberry

from python_graph.db.connection import (
    DBConnection
)
from python_graph.validation import (
    VALIDATORS
)
from python_graph.constant import (
    ACTIONS,
    INSERT_ACTIONS,
    MODELS,
    BOOKS_FIELDNAMES,
    PERSONS_FIELDNAMES,
    MODELS_TEXT,

)
from python_graph.models import (
    Query,
    Mutation,
)
from python_graph.models.core import (
    CustomContext,
)




def create_tables(connection: DBConnection):
    connection.execute_sql_file("database.sql")


def check_table_creation():
    with sqlite3.connect("graphql_sqlite.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(table[0])


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
    return globals().get(f"{model_name.upper()}_FIELDNAMES")


def consult(schema: strawberry.Schema, context=None):
    model = _ask_working_model()
    fields_types = _get_fieldnames(model)
    fields = [field for field, _ in fields_types]
    fields_asked = _ask_fieldnames(fields)
    query_2 = f"query {{ {model} {{ {', '.join(fields_asked)} }} }}"
    return schema.execute_sync(query_2, context_value=context)


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

            print(
                f"Invalid value for field {field}. "
                f"Expected type: {type_field.__name__}")

    return data


def insert(schema: strawberry.Schema, context=None):
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
    return schema.execute_sync(mutation, context_value=context)


def main():
    conn = DBConnection()
    context = CustomContext(db=conn)
    # create_tables(conn)
    # check_table_creation()

    action = input("""What do you want to do?:
1. Insert
2. Consult
Select: """).strip().lower()

    if action not in ACTIONS:
        print("Invalid action.")
        sys.exit(0)

    schema = strawberry.Schema(
        query=Query,
        mutation=Mutation,
    )
    result = globals()[ACTIONS[action]](schema, context)
    print(json.dumps(result.data, indent=4))


if __name__ == "__main__":
    print("Starting GraphQL SQLite Client...")
    main()
