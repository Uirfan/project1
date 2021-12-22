class User:
    def __init__(self, user_id: int, hashed_user: str, first_name: str, last_name: str, is_manager: bool):
        self.user_id = user_id
        self.hashed_user = hashed_user
        self.first_name = first_name
        self.last_name = last_name
        self.is_manager = is_manager

    def make_user_dictionary(self):
        return {
            "userId": self.user_id,
            "userHash": self.hashed_user,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "isManager": self.is_manager

        }
