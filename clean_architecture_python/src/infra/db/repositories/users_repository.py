from src.infra.db.settings.connection import DBConnectionHandle
from src.infra.db.entites.users import Users as UsersEntity

class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name:str, age: int) -> None:
        with DBConnectionHandle() as database:
            try:
                new_registry = UsersEntity(
                    first_name=first_name,
                    last_name = last_name,
                    age = age
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception