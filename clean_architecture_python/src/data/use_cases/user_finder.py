from typing import Dict
from src.domain.user_cases.user_finder import UserFinder as UserFinderInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        pass