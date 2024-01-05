from flask import session
import requests
from app.utils import helper

baseUri = helper.userServiceUri()

def login(data):
  response = requests.post(baseUri+'/auth/login', data=data)
  if response.status_code == 200:
    session['token'] = response.json()['result']['access_token']
  else:
    session['token'] = ''
  return response.json()

def userLogin():
  response = requests.get(baseUri+'/auth/user', headers={'Authorization': 'Bearer '+session.get('token')})
  return response.json()