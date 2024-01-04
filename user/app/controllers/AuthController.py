from app.utils import response
from flask import request
from app.services import AuthService

def login():
  try:
    data = AuthService.login(request.form)
    if not data['status']:
      return response.error([], data['message'])
    return response.success(data, "Successfully login")
  except Exception as e:
    return response.error(str(e))

def userLogin():
  try:
    data = AuthService.userLogin()
    return response.success(data, "Successfully get user login")
  except Exception as e:
    return response.error(str(e))