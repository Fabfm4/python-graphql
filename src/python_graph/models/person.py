import typing
import strawberry

from python_graph.models.core import CustomContext


@strawberry.type
class Person:
    id: int
    name: str
    age: int
    height: float
    is_student: bool


@strawberry.type
class PersonMutation:

    @strawberry.mutation
    def add_person(self, name: str, age: int, height: float,
                   is_student: bool, info: strawberry.Info[CustomContext]) -> Person:
        db = info.context.db
        with db.Session() as session:
            session.execute(
                db.sa.text("INSERT INTO persons (name, age, height, is_student) VALUES (:name, :age, :height, :is_student)"),
                {"name": name, "age": age, "height": height, "is_student": int(is_student)},
            )
            result = session.execute(
                db.sa.text("SELECT last_insert_rowid()")).scalar_one()
            session.commit()
            return Person(
                id=result, name=name,
                age=age, height=height,
                is_student=is_student)


@strawberry.type
class PersonQuery:

    @strawberry.field
    def persons(self, info: strawberry.Info[CustomContext]) -> typing.List[Person]:
        db = info.context.db
        with db.Session() as session:
            print("Fetching persons from database...")
            result = session.execute(
                db.sa.text(
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
