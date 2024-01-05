from app.services import UserService

def index():
  return UserService.getUsers()

def show(id):
  return UserService.getUser(id)

def create(data):
  return UserService.storeUser(data)

def update(id, data):
  return UserService.updateUser(id, data)

def delete(id):
  return UserService.deleteUser(id)