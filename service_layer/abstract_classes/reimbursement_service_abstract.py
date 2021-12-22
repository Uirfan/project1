from abc import ABC, abstractmethod
from entities.reimbursement import Reimbursement


class ReimbursementServiceABS(ABC):

    @abstractmethod
    def service_create_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_get_reimbursement(self, *vargs):
        pass

    @abstractmethod
    def service_get_reimbursement_by_user_id(self, user_id):
        pass

    @abstractmethod
    def service_update_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_delete_reimbursement(self, *vargs):
        pass
