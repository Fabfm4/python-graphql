import strawberry

from .book import BookQuery, BookMutation
from .person import PersonQuery, PersonMutation


@strawberry.type
class Query(BookQuery, PersonQuery):
    pass


@strawberry.type
class Mutation(BookMutation, PersonMutation):
    pass
