from src.infra.db.settings.connection import DBConnectionHandle
from src.infra.db.entites.users import Users as UsersEntity
import typing as t

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

    @classmethod
    def select_user(cls, first_name: str) -> t.Any:
        with DBConnectionHandle() as database:
            try:
                users = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.first_name == first_name)
                        .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception