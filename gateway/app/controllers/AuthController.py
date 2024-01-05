from app.services import AuthService

def login(data):
  return AuthService.login(data)

def userLogin():
  return AuthService.userLogin()