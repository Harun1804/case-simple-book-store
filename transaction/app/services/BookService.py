import requests

def getBookById(id):
  url = 'http://localhost:5001/books/' + str(id)
  response = requests.get(url)
  return response.json()['result']

def updateBookAvailability(id, is_available):
  url = 'http://localhost:5001/books/availability/' + str(id)
  data = {
    'is_available': is_available
  }
  response = requests.put(url, data=data)
  return response.json()