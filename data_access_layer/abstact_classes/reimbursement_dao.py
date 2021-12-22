from abc import ABC, abstractmethod

from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):
    @abstractmethod
    def create_reimbursement_dao(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def get_reimbursement_dao(self, *argv):
        pass

    @abstractmethod
    def update_reimbursement_dao(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def delete_reimbursement_dao(self, *argv):
        pass
