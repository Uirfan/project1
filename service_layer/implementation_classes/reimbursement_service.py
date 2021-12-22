from service_layer.abstract_classes.reimbursement_service_abstract import ReimbursementServiceABS
from entities.reimbursement import Reimbursement
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp


class ReimbursementService(ReimbursementServiceABS):
    def __init__(self, reimbursement_dao: ReimbursementDAOImp):
        self.reimbursement_dao = reimbursement_dao

    def service_create_reimbursement(self, reimbursement: Reimbursement):
        return self.reimbursement_dao.create_reimbursement_dao(reimbursement)

    def service_get_reimbursement(self, *vargs):
        return self.reimbursement_dao.get_reimbursement_dao(*vargs)

    def service_get_reimbursement_by_user_id(self, user_id: int):
        return self.reimbursement_dao.get_reimbursement_by_user_id(user_id)

    def service_update_reimbursement(self, reimbursement_id: int, status: str, reject_reason: str):
        got = self.service_get_reimbursement(reimbursement_id)
        got[0].status = status
        got[0].reject_reason = reject_reason
        return self.reimbursement_dao.update_reimbursement_dao(got[0])

    def service_delete_reimbursement(self, *vargs):
        return self.reimbursement_dao.delete_reimbursement_dao(*vargs)
