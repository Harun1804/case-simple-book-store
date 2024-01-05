import os

basedir = os.path.abspath(os.path.dirname(__file__))

def bookServiceUri():
  return str(os.environ.get('BOOK_SERVICE_URI'))

def userServiceUri():
  return str(os.environ.get('USER_SERVICE_URI'))

def transactionServiceUri():
  return str(os.environ.get('TRANSACTION_SERVICE_URL'))

def appSecretKey():
  return str(os.environ.get('APP_SECRET_KEY'))