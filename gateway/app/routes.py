from app import app
from flask import request
from app.controllers import BookController
from flask_jwt_extended import jwt_required

@app.route('/master/books', methods=['GET', 'POST'])
@jwt_required()
def books():
  if request.method == 'GET':
    return BookController.index()
  elif request.method == 'POST':
    return BookController.create(request.form)

@app.route('/master/books/<id>', methods=['GET','PUT','DELETE'])
@jwt_required()
def book(id):
  if request.method == 'GET':
    return BookController.show(id)
  elif request.method == 'PUT':
    return BookController.update(id, request.form)
  elif request.method == 'DELETE':
    return BookController.delete(id)