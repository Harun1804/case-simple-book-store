from app import app
from flask import request
from app.controllers import UserController, AuthController
from flask_jwt_extended import jwt_required

@app.route('/users', methods=['GET','POST'])
def users():
  if request.method == 'GET':
    return UserController.index()
  elif request.method == 'POST':
    return UserController.store()

@app.route('/users/<id>', methods=['GET','PUT','DELETE'])
def user(id):
  if request.method == 'GET':
    return UserController.show(id)
  elif request.method == 'PUT':
    return UserController.update(id)
  elif request.method == 'DELETE':
    return UserController.delete(id)

@app.route('/auth/login', methods=['POST'])
def login():
  return AuthController.login()

@app.route('/auth/user', methods=['GET'])
@jwt_required()
def userLogin():
  return AuthController.userLogin()