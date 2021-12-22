from entities.reimbursement import Reimbursement
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp

reimbursement_dao = ReimbursementDAOImp()
reimbursement1 = Reimbursement(0, 2, "Gas",
                               "Hello, yesterday I went to pickup a replacement part for the boiler. It was 400km away"
                               , 100, 0, 0, 0, 0)
reimbursement_update = Reimbursement(3, 2, "Gas",
                                     "Hello, yesterday I went to pickup a replacement part for the boiler. It was "
                                     "400km away "
                                     , 100, 0, "rejected", "Everybody knows you own a tesla", 0)


def test_dao_create_reimbursement():
    returned_reimbursement = reimbursement_dao.create_reimbursement_dao(reimbursement1)
    assert returned_reimbursement.reimbursement_id != 0


def test_dao_get_reimbursement():
    returned_reimbursement = reimbursement_dao.get_reimbursement_dao(3)
    assert returned_reimbursement[0].reimbursement_id != 0


def test_dao_update_reimbursement():
    updated_reimbursement = reimbursement_dao.update_reimbursement_dao(reimbursement_update)
    assert updated_reimbursement.status == "rejected"


def test_dao_delete_reimbursement():
    returned_bol = reimbursement_dao.delete_reimbursement_dao(1)
    assert returned_bol == True
