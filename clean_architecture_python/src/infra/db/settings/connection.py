from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandle:

    def __init__(self) -> None:
        self.__connection_string = "postgresql://admin:admin@localhost:5432/postgres"

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine


    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.engine)
        self.session = session_make()
        return self

    def __exit__(self):
        self.session.close()