from app import app
from flask import request
from app.controllers import BookController

@app.route('/books', methods=['GET','POST'])
def books():
  if request.method == 'GET':
    return BookController.index()
  elif request.method == 'POST':
    return BookController.store()

@app.route('/books/<id>', methods=['GET','PUT','DELETE'])
def book(id):
  if request.method == 'GET':
    return BookController.show(id)
  elif request.method == 'PUT':
    return BookController.update(id)
  elif request.method == 'DELETE':
    return BookController.delete(id)
