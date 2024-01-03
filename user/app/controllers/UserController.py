from app.utils import response
from flask import request
from app.services import UserService

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
      return response.error("User Not Found", 404)
    return response.success(user, "Success Get User")
  except Exception as e:
    return response.error(str(e))

def store():
  try:
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    UserService.storeUser(username, password, role)
    return response.success([], "User Has Been Created")
  except Exception as e:
    return response.error(str(e))

def update(id):
  try:
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