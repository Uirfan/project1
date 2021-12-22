from data_access_layer.abstact_classes.user_dao import UserDAO
from entities.user import User
from util.database_connection import connection


class UserDAOImp(UserDAO):
    def create_user_dao(self, user: User) -> User:
        sql = 'insert into "project1".users values(default, %s, %s, %s, %s) returning user_id'
        cursor = connection.cursor()
        cursor.execute(sql, (
            user.hashed_user,
            user.first_name,
            user.last_name,
            user.is_manager))
        connection.commit()
        user_id = cursor.fetchone()[0]
        user.user_id = user_id
        return user

    def get_user_dao(self, *argv):
        return_list = []
        for a in argv:
            if type(a) is int:
                sql = 'select * from "project1".users where user_id = %s'
                cursor = connection.cursor()
                cursor.execute(sql, [a])
                user_record = cursor.fetchone()
                return_list.append(User(*user_record))
            elif a == "all":
                sql = 'select * from "project1".users'
                cursor = connection.cursor()
                cursor.execute(sql)
                user_record = cursor.fetchall()
                for b in user_record:
                    return_list.append(User(*b))
        if len(return_list) < 2:
            return return_list[0]
        else:
            return return_list

    def update_user_dao(self, user: User):
        sql = 'update "project1".users set ' \
              'hashed_user = %s, ' \
              'first_name = %s, ' \
              'last_name =%s, ' \
              'is_manager =%s ' \
              'where user_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (
            user.hashed_user,
            user.first_name,
            user.last_name,
            user.is_manager,
            user.user_id))
        connection.commit()
        return user

    def delete_user_dao(self, *argv):
        for a in argv:
            if type(a) is int:
                sql = 'delete from "project1".users where user_id = %s'
                cursor = connection.cursor()
                cursor.execute(sql, [a])
                connection.commit()

            elif a == "all":
                sql = 'delete from "project1".users'
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
        return True
