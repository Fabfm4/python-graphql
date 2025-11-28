import typing
import strawberry

from python_graph.models.core import CustomContext


@strawberry.type
class Book:
    id: int
    title: str
    author: str


@strawberry.type
class BookQuery:

    @strawberry.field
    def books(self, info: strawberry.Info[CustomContext]) -> typing.List[Book]:
        db = info.context.db
        with db.Session() as session:
            print("Fetching books from database...")
            result = session.execute(db.sa.text("SELECT id, title, author FROM books")).mappings().all()
            books = [Book(id=row["id"], title=row["title"], author=row["author"]) for row in result]
            return books


@strawberry.type
class BookMutation:

    @strawberry.mutation
    def add_book(self, title: str, author: str, info: strawberry.Info[CustomContext]) -> Book:
        db = info.context.db
        with db.Session() as session:
            session.execute(
                db.sa.text("INSERT INTO books (title, author) VALUES (:title, :author)"),
                {"title": title, "author": author},
            )
            result = session.execute(db.sa.text("SELECT last_insert_rowid()")).scalar_one()
            session.commit()
            return Book(id=result, title=title, author=author)
