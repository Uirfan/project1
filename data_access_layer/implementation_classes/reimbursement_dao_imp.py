from data_access_layer.abstact_classes.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class ReimbursementDAOImp(ReimbursementDAO):
    def create_reimbursement_dao(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'insert into "project1".reimbursements values(default, %s, %s, %s, %s, default, default, default, ' \
              'default) returning reimbursement_id '
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.user_id,
            reimbursement.expense_name,
            reimbursement.expense_reason,
            reimbursement.expense_amount

            ))
        connection.commit()
        reimbursement.reimbursement_id = cursor.fetchone()[0]
        return reimbursement

    def get_reimbursement_dao(self, *argv):
        return_list = []
        for a in argv:
            if type(a) is int:
                sql = 'select * from "project1".reimbursements where reimbursement_id = %s'
                cursor = connection.cursor()
                cursor.execute(sql, [a])
                reimbursement_record = cursor.fetchone()
                return_list.append(Reimbursement(*reimbursement_record))
            elif a == "all":
                sql = 'select * from "project1".reimbursements'
                cursor = connection.cursor()
                cursor.execute(sql)
                reimbursement_record = cursor.fetchall()
                for b in reimbursement_record:
                    return_list.append(Reimbursement(*b))
            elif a == "pending":
                sql = 'select * from "project1".reimbursements where status = %s'
                cursor = connection.cursor()
                cursor.execute(sql, [a])
                reimbursement_record = cursor.fetchall()
                for b in reimbursement_record:
                    return_list.append(Reimbursement(*b))
            elif a == "accepted":
                sql = 'select * from "project1".reimbursements where status = %s'
                cursor = connection.cursor()
                cursor.execute(sql, [a])
                reimbursement_record = cursor.fetchall()
                for b in reimbursement_record:
                    return_list.append(Reimbursement(*b))
            elif a == "rejected":
                sql = 'select * from "project1".reimbursements where status = %s'
                cursor = connection.cursor()
                cursor.execute(sql, [a])
                reimbursement_record = cursor.fetchall()
                for b in reimbursement_record:
                    return_list.append(Reimbursement(*b))
            else:
                return "Invalid Argument"
        return return_list

    def get_reimbursement_by_user_id(self, user_id: int):
        sql = 'select * from "project1".reimbursements where user_id = %s'
        return_list = []
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        reimbursement_record = cursor.fetchall()
        for b in reimbursement_record:
            return_list.append(Reimbursement(*b))
        return return_list

    def update_reimbursement_dao(self, reimbursement: Reimbursement):
        sql = 'update "project1".reimbursements set user_id = %s, expense_name = %s, expense_reason = %s, ' \
              'expense_amount = %s, status =%s, reject_reason =%s, status_date = CURRENT_DATE where reimbursement_id ' \
              '= %s returning status '
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.user_id,
            reimbursement.expense_name,
            reimbursement.expense_reason,
            reimbursement.expense_amount,
            reimbursement.status,
            reimbursement.reject_reason,
            reimbursement.reimbursement_id))
        connection.commit()
        reimbursement.status = cursor.fetchone()[0]
        return reimbursement

    def delete_reimbursement_dao(self, *argv):
        for a in argv:
            if type(a) is int:
                sql = 'delete from "project1".reimbursements where reimbursement_id = %s'
                cursor = connection.cursor()
                cursor.execute(sql, [a])
                connection.commit()
            elif a == "all":
                sql = 'delete from "project1".reimbursements'
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
            else:
                return "Invalid Argument"
        return True
