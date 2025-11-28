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
BOOKS_FIELDNAMES = [
    ("id", int),
    ("title", str),
    ("author", str)
]
PERSONS_FIELDNAMES = [
    ("id", int),
    ("name", str),
    ("age", int),
    ("height", float),
    ("isStudent", bool)
]
MODELS_TEXT = """
1. Books
2. Persons
"""
