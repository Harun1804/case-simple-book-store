from flask import Blueprint, request
from app.controllers import UserController
from flask_jwt_extended import jwt_required

blueprint = Blueprint('user', __name__, url_prefix='/master/users')

@blueprint.route('', methods=['GET', 'POST'])
@jwt_required()
def users():
  if request.method == 'GET':
    return UserController.index()
  elif request.method == 'POST':
    return UserController.create(request.form)

@blueprint.route('/<id>', methods=['GET','PUT','DELETE'])
@jwt_required()
def user(id):
  if request.method == 'GET':
    return UserController.show(id)
  elif request.method == 'PUT':
    return UserController.update(id, request.form)
  elif request.method == 'DELETE':
    return UserController.delete(id)