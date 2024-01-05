from app import db
from app.models.user import User
from app.services.UserService import singleTransform
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from datetime import timedelta

def login(data):
  user = User.query.filter_by(username=data['username']).first()
  if not user:
    return {
      'message': 'User not found',
      'status': False
    }

  if not user.checkPassword(data['password']):
    return {
      'message': 'Password is wrong',
      'status': False
    }

  data = singleTransform(user)
  expires = timedelta(days=7)
  expiores_refresh = timedelta(days=7)
  access_token = create_access_token(data, expires_delta=expires)
  refresh_token = create_refresh_token(data, expires_delta=expiores_refresh)

  return {
    'access_token': access_token,
    'refresh_token': refresh_token,
    'type': 'Bearer',
    'user': data,
    'status': True
  }

def userLogin():
  return get_jwt_identity()
