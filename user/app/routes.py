from app import app
from flask import request
from app.controllers import UserController

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