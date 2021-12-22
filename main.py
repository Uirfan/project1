from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from data_access_layer.implementation_classes.user_dao_imp import UserDAOImp
from service_layer.implementation_classes.reimbursement_service import ReimbursementService
from service_layer.implementation_classes.user_service import UserService
from entities.reimbursement import Reimbursement
from entities.user import User
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

logging.basicConfig(filename='records.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')
app = Flask(__name__)
user_dao = UserDAOImp()
reimbursement_dao = ReimbursementDAOImp()
user_service = UserService(user_dao)
reimbursement_service = ReimbursementService(reimbursement_dao)

CORS(app)


###################################################################################


@app.get("/user/get")
def get_users():
    requested = request.get_json()
    returned_users = user_service.service_get_user(requested["users"])
    if type(returned_users) == User:
        return returned_users.make_user_dictionary()
    else:
        returned_users_dic_list = []
        for a in returned_users:
            returned_users_dic_list.append(a.make_user_dictionary())
        return jsonify(returned_users_dic_list)


@app.post("/user/validate")
def validate_users():
    requested = request.get_json()
    return_check = user_service.service_validate_user(requested["userName"], requested["password"])
    if type(return_check) == User:
        return_dic = {"userId": return_check.user_id,
                      "lastName": return_check.last_name,
                      "firstName": return_check.first_name,
                      "isManager": return_check.is_manager}
        return jsonify(return_dic)
    else:
        return_dic = {"Message": "Invalid Information"}
        return jsonify(return_dic)


@app.post("/user/create")
def create_user():
    try:
        requested = request.get_json()

        return_user = user_service.service_create_user(
            str(requested["userName"]),
            str(requested["password"]),
            str(requested["firstName"]),
            str(requested["lastName"]),
            bool(requested["isManager"]))
        return jsonify(return_user.make_user_dictionary())
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.post("/user/update")
def update_user():
    try:
        requested = request.get_json()
        returned_user = user_service.service_update_user(
            int(requested["userId"]),
            str(requested["userName"]),
            str(requested["password"]),
            str(requested["firstName"]),
            str(requested["lastName"]),
            bool(requested["isManager"]))
        return jsonify(returned_user.make_user_dictionary())
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.delete("/user/delete")
def delete_users():
    requested = request.get_json()
    if user_service.service_delete_user(requested["users"]):
        return "Success"


###################################################################################

@app.post("/reimbursement/get")
def get_reimbursements():
    returned_reimbursement_dic_list = []
    requested = request.get_json()
    returned_reimbursements = reimbursement_service.service_get_reimbursement(requested["reimbursements"])
    if type(returned_reimbursements) == Reimbursement:
        returned_reimbursement_dic_list.append(returned_reimbursements.make_reimbursement_dictionary())
        return jsonify(returned_reimbursement_dic_list)
    else:
        for a in returned_reimbursements:
            returned_reimbursement_dic_list.append(a.make_reimbursement_dictionary())
        return jsonify(returned_reimbursement_dic_list)

@app.post("/reimbursement/getByUserId")
def get_reimbursements_by_id():
    returned_reimbursement_dic_list = []
    requested = request.get_json()
    returned_reimbursements = reimbursement_service.service_get_reimbursement_by_user_id(requested["reimbursements"])
    if type(returned_reimbursements) == Reimbursement:
        returned_reimbursement_dic_list.append(returned_reimbursements.make_reimbursement_dictionary())
        return jsonify(returned_reimbursement_dic_list)
    else:
        for a in returned_reimbursements:
            returned_reimbursement_dic_list.append(a.make_reimbursement_dictionary())
        return jsonify(returned_reimbursement_dic_list)

@app.post("/reimbursement/create")
def create_reimbursement():
    try:
        requested = request.get_json()
        new_reimbursement = Reimbursement(0,
                                          int(requested["userId"]),
                                          str(requested["expenseName"]),
                                          str(requested["expenseReason"]),
                                          float(requested["expenseAmount"]),
                                          0, 0, 0, 0
                                          )
        return_reimbursement = reimbursement_service.service_create_reimbursement(new_reimbursement)
        return jsonify(return_reimbursement.make_reimbursement_dictionary())
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.post("/reimbursement/update")
def update_reimbursement():
    try:
        requested = request.get_json()
        returned_reimbursement = reimbursement_service.service_update_reimbursement(int(requested["reimbursementId"]),
                                                                                    str(requested["status"]),
                                                                                    str(requested["rejectReason"]))
        return jsonify(returned_reimbursement.make_reimbursement_dictionary())
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.delete("/reimbursement/delete")
def delete_reimbursements():
    requested = request.get_json()
    if reimbursement_service.service_delete_reimbursement(requested["reimbursements"]):
        return "Success"


app.run()
