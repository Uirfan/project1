from custom_exceptions.custom_exception_message import CustomExceptionMessage
from service_layer.implementation_classes.user_service import UserService
from data_access_layer.implementation_classes.user_dao_imp import UserDAOImp

userDao = UserDAOImp()
UserServices = UserService(userDao)


def test_service_validate_user():
    got_user = UserServices.service_validate_user("styphon31", "4321")
    assert got_user.user_id != 0


def test_service_create_user():
    created_user = UserServices.service_create_user("Test", "1234", "Service", "Test", False)
    assert created_user.user_id != 0


def test_service_update_user():
    try:
        UserServices.service_update_user(0, "test", "test", "test", "test", False)

    except CustomExceptionMessage as e:
        assert str(e) == "User not found"
