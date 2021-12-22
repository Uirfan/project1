class Reimbursement:
    def __init__(self, reimbursement_id: int, user_id: int, expense_name: str, expense_reason: str,
                 expense_amount: float, date, status: str, reject_reason: str, status_date):
        self.reimbursement_id = int(reimbursement_id)
        self.user_id = int(user_id)
        self.expense_name = expense_name
        self.expense_reason = expense_reason
        self.expense_amount = float(expense_amount)
        self.date = date
        self.status = status
        self.reject_reason = reject_reason
        self.status_date = status_date

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "userId": self.user_id,
            "expenseName": self.expense_name,
            "expenseReason": self.expense_reason,
            "expenseAmount": self.expense_amount,
            "date": self.date,
            "status": self.status,
            "rejectReason": self.reject_reason,
            "statusDate": self.status_date

        }
