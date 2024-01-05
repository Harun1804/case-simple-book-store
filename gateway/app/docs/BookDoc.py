from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from app.controllers import BookController
from http import HTTPStatus

api = Namespace('Book', description='Book service from bookstore microservice')
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, location='form')
parser.add_argument('author', type=str, required=True, location='form')
parser.add_argument('publisher', type=str, required=True, location='form')
parser.add_argument('year', type=int, required=True, location='form')
parser.add_argument('is_available', type=int, required=True, location='form')

parser2 = reqparse.RequestParser()
parser2.add_argument('is_available', type=int, required=True, location='form')

bookModel = api.model('Book', {
  'title': fields.String(required=True),
  'author': fields.String(required=True),
  'publisher': fields.String(required=True),
  'year': fields.Integer(required=True),
  'is_available': fields.Boolean(required=True)
})

bookResponseModel = api.model('BookResponse', {
  'message': fields.String(description='Response message'),
  'result': fields.Nested(bookModel)
})

@api.route('')
class Books(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.marshal_list_with(bookResponseModel)
  def get(self):
    return BookController.index()
  
  @api.response(201, 'Book has been created')
  @api.response(401, 'Unauthorized')
  @api.response(422, 'Validation Error')
  @api.expect(parser, validate=True)
  @api.marshal_with(bookModel, code=HTTPStatus.CREATED)
  def post(self):
    parser.parse_args()
    return BookController.create(request.form)

@api.route('/<id>')
class Book(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'Book not found')
  @api.marshal_with(bookResponseModel)
  def get(self, id):
    return BookController.show(id)
  
  @api.response(200, 'Book has been updated')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'Book not found')
  @api.response(422, 'Validation Error')
  @api.expect(parser, validate=True)
  @api.marshal_with(bookModel)
  def put(self, id):
    parser.parse_args()
    return BookController.update(id, request.form)
  
  @api.response(200, 'Book has been deleted')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'Book not found')
  @api.marshal_with(bookModel)
  def delete(self, id):
    return BookController.delete(id)

@api.route('/availability')
class AvailableBooks(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.marshal_list_with(bookResponseModel)
  def get(self):
    return BookController.getAvailableBooks()

@api.route('/availability/<id>')
class UpdateAvailableBook(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'Book not found')
  @api.response(422, 'Validation Error')
  @api.expect(parser2, validate=True)
  @api.marshal_with(bookModel)
  def put(self, id):
    parser2.parse_args()
    return BookController.updateAvailableBook(id, request.form)