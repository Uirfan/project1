from abc import ABC, abstractmethod

from entities.user import User


class UserDAO(ABC):
    @abstractmethod
    def create_user_dao(self, user: User):
        pass

    @abstractmethod
    def get_user_dao(self, *argv):
        pass

    @abstractmethod
    def update_user_dao(self, user_id: int):
        pass

    @abstractmethod
    def delete_user_dao(self, *vargs):
        pass
