from flask import Blueprint, request
from app.controllers import BookController
from flask_jwt_extended import jwt_required

blueprint = Blueprint('book', __name__, url_prefix='/master/books')
@blueprint.route('', methods=['GET', 'POST'])
@jwt_required()
def books():
  if request.method == 'GET':
    return BookController.index()
  elif request.method == 'POST':
    data = {
      'title': request.form.get('title'),
      'author': request.form.get('author'),
      'publisher': request.form.get('publisher'),
      'year': request.form.get('year'),
      'is_available': request.form.get('is_available'),
    }
    files = {
      'thumbnail': request.files.get('thumbnail')
    }
    return BookController.create(data, files)

@blueprint.route('/<id>', methods=['GET','PUT','DELETE'])
@jwt_required()
def book(id):
  if request.method == 'GET':
    return BookController.show(id)
  elif request.method == 'PUT':
    data = {
      'title': request.form.get('title'),
      'author': request.form.get('author'),
      'publisher': request.form.get('publisher'),
      'year': request.form.get('year'),
      'is_available': request.form.get('is_available'),
    }

    files = {
      'thumbnail': request.files.get('thumbnail')
    }

    if files['thumbnail'] is None:
      return BookController.update(id, data, files)
    else: 
      return BookController.update(id, data)
  elif request.method == 'DELETE':
    return BookController.delete(id)

@blueprint.route('/availability', methods=['GET'])
@jwt_required()
def availableBooks():
  return BookController.getAvailableBooks()

@blueprint.route('/availability/<id>', methods=['PUT'])
@jwt_required()
def updateAvailableBook(id):
  return BookController.updateAvailableBook(id, request.form)