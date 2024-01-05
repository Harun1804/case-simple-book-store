import requests
from app.utils import helper

baseUri = helper.userServiceUri()

def getUsers():
  response = requests.get(baseUri+'/users')
  return response.json()

def getUser(id):
  response = requests.get(baseUri+'/users/'+str(id))
  return response.json()

def storeUser(data):
  response = requests.post(baseUri+'/users', data=data)
  return response.json()

def updateUser(id, data):
  response = requests.put(baseUri+'/users/'+str(id), data=data)
  return response.json()

def deleteUser(id):
  response = requests.delete(baseUri+'/users/'+str(id))
  return response.json()