from flask import Blueprint, request
from app.controllers import TransactionController
from flask_jwt_extended import jwt_required

blueprint = Blueprint('transaction', __name__, url_prefix='/transactions')

@blueprint.route('', methods=['GET', 'POST'])
@jwt_required()
def transactions():
  if request.method == 'GET':
    return TransactionController.index()
  elif request.method == 'POST':
    return TransactionController.create(request.json)
  
@blueprint.route('/<id>', methods=['GET','PUT','DELETE'])
@jwt_required()
def transaction(id):
  if request.method == 'GET':
    return TransactionController.show(id)
  elif request.method == 'PUT':
    return TransactionController.update(id, request.form)
  elif request.method == 'DELETE':
    return TransactionController.delete(id)