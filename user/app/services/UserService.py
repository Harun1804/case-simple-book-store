from app import db
from app.models.user import User
from app.utils import formatter

def getUsers():
  users = User.query.all()
  data = formatter.formatArray(users, singleTransform)
  return data

def getUser(id):
  user = User.query.filter_by(id=id).first()
  if not user:
    return False
  data = singleTransform(user)
  return data

def storeUser(username, password, role):
  user = User(username=username, role=role)
  user.setPassword(password)
  db.session.add(user)
  db.session.commit()

def updateUser(id, username, password = '', role = ''):
  user = User.query.filter_by(id=id).first()
  user.username = username
  user.role = role
  if password != '':
    user.setPassword(password)
  db.session.commit()

def deleteUser(id):
  user = User.query.filter_by(id=id).first()
  if not user:
    return False
  db.session.delete(user)
  db.session.commit()

def singleTransform(data):
  data = {
    'id': data.id,
    'username': data.username,
    'role': data.role,
  }

  return data
