from flask import Blueprint, request
from app.controllers import AuthController
from flask_jwt_extended import jwt_required

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/login', methods=['POST'])
def login():
  return AuthController.login(request.form)

@blueprint.route('/user', methods=['GET'])
@jwt_required()
def userLogin():
  return AuthController.userLogin()