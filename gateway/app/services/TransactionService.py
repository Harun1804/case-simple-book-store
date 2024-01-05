import requests
from app.utils import helper

baseUri = helper.transactionServiceUri()

def getTransactions():
  response = requests.get(baseUri+'/transactions')
  return response.json()

def getTransaction(id):
  response = requests.get(baseUri+'/transactions/'+str(id))
  return response.json()

def storeTransaction(data):
  response = requests.post(baseUri+'/transactions', json=data)
  return response.json()

def updateTransaction(id, data):
  response = requests.put(baseUri+'/transactions/'+str(id), data=data)
  return response.json()

def deleteTransaction(id):
  response = requests.delete(baseUri+'/transactions/'+str(id))
  return response.json()