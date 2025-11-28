import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


class DBConnection:

    def __init__(self):
        self.engine = sa.create_engine("sqlite:///graphql_sqlite.db")
        self.Session = sessionmaker(bind=self.engine)
        self.sa = sa

    def execute_sql_file(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_commands = file.read()
        with self.engine.connect() as connection:
            for command in sql_commands.split(';'):
                cmd = command.strip()
                if cmd:
                    connection.execute(sa.text(cmd))
            connection.commit()
