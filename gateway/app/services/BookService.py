import requests

def get_books():
  response = requests.get('http://localhost:5001/books')
  return response.json()