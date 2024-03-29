import requests
from app.utils import helper

baseUri = helper.bookServiceUri()

def get_books():
  response = requests.get(baseUri+'/books')
  return response.json()

def get_book(id):
  response = requests.get(baseUri+'/books/'+str(id))
  return response.json()

def create_book(data, files):
  response = requests.post(baseUri+'/books', data=data, files=files)
  return response.json()

def update_book(id, data, files=None):
  if files is None:
    print(files)
    response = requests.put(baseUri+'/books/'+str(id), data=data)
  else:
    response = requests.put(baseUri+'/books/'+str(id), data=data, files=files)
  return response.json()

def delete_book(id):
  response = requests.delete(baseUri+'/books/'+str(id))
  return response.json()

def getAvailableBooks():
  response = requests.get(baseUri+'/books/availability')
  return response.json()

def updateAvailableBook(id, data):
  response = requests.put(baseUri+'/books/availability/'+str(id), data=data)
  return response.json()