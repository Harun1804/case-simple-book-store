from app.utils import response
from flask import request
from app.services import UserService
from app.validations import UserValidation

def index():
  try:
    users = UserService.getUsers()
    return response.success(users, "Success Get Users")
  except Exception as e:
    return response.error(str(e))

def show(id):
  try:
    user = UserService.getUser(id)
    if not user:
      return response.error("User Not Found", status=404)
    return response.success(user, "Success Get User")
  except Exception as e:
    return response.error(str(e))

def store():
  try:
    validation = UserValidation.UserValidation()
    errors = validation.validate(request.form)
    if errors:
      return response.validateError(errors)

    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    UserService.storeUser(username, password, role)
    return response.success([], "User Has Been Created", 201)
  except Exception as e:
    return response.error(str(e))

def update(id):
  try:
    user = UserService.getUser(id)
    if not user:
      return response.error("User Not Found", 404)

    validation = UserValidation.UserValidation()
    validation.context = {'id': id}
    errors = validation.validate(request.form, partial=('password',))
    if errors:
      return response.validateError(errors)

    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    UserService.updateUser(id, username, password, role)
    return response.success([], "User Has Been Updated")
  except Exception as e:
    return response.error(str(e))

def delete(id):
  try:
    user = UserService.getUser(id)
    if not user:
      return response.error("User Not Found", 404)
    UserService.deleteUser(id)
    return response.success([], "User Has Been Deleted")
  except Exception as e:
    return response.error(str(e))