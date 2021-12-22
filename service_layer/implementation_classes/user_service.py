import hashlib
from service_layer.abstract_classes.user_service_abstract import UserServiceABS
from entities.user import User
from data_access_layer.implementation_classes.user_dao_imp import UserDAOImp
from custom_exceptions.custom_exception_message import CustomExceptionMessage


class UserService(UserServiceABS):
    def __init__(self, user_dao: UserDAOImp):
        self.user_dao = user_dao

    def service_validate_user(self, user_name: str, password: str):
        user_string = user_name + password
        encoded_user = user_string.encode()
        hashed_user = hashlib.sha256(encoded_user).hexdigest()
        all_users = self.service_get_user("all")
        for a in all_users:
            if a.hashed_user == hashed_user:
                return a
        return False

    def service_create_user(self, user_name: str, password: str, first_name: str, last_name, is_manager: bool):
        user_string = user_name + password
        encoded_user = user_string.encode()
        hashed_user = hashlib.sha256(encoded_user).hexdigest()
        user = User(0, hashed_user, first_name, last_name, is_manager)
        return self.user_dao.create_user_dao(user)

    def service_get_user(self, *vargs):
        return self.user_dao.get_user_dao(*vargs)

    def service_update_user(self, user_id: int, user_name: str, password: str, first_name: str, last_name: str,
                            is_manager: bool):
        all_users = self.service_get_user("all")
        for a in all_users:
            if a.user_id == user_id:
                user_string = user_name + password
                encoded_user = user_string.encode()
                hashed_user = hashlib.sha256(encoded_user).hexdigest()
                user = User(user_id, hashed_user, first_name, last_name, is_manager)
                return self.user_dao.update_user_dao(user)
        raise CustomExceptionMessage("User not found")

    def service_delete_user(self, *vargs):
        return self.user_dao.delete_user_dao(*vargs)
