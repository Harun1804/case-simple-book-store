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
    return BookController.create(request.form)

@blueprint.route('/<id>', methods=['GET','PUT','DELETE'])
@jwt_required()
def book(id):
  if request.method == 'GET':
    return BookController.show(id)
  elif request.method == 'PUT':
    return BookController.update(id, request.form)
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