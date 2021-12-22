from abc import ABC, abstractmethod
from entities.user import User


class UserServiceABS(ABC):

    @abstractmethod
    def service_validate_user(self, user_name: str, password: str):
        pass

    @abstractmethod
    def service_create_user(self, user_name: str, password: str, first_name: str, last_name, is_manager: bool):
        pass

    @abstractmethod
    def service_get_user(self, *vargs):
        pass

    @abstractmethod
    def service_update_user(self, user_id: int,user_name: str, password: str, first_name: str, last_name, is_manager: bool):
        pass

    @abstractmethod
    def service_delete_user(self, *vargs):
        pass
