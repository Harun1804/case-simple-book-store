from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from app.controllers import UserController
from http import HTTPStatus

api = Namespace('User', description='User service from user microservice')
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, location='form')
parser.add_argument('password', type=str, required=True, location='form')
parser.add_argument('role', type=str, required=True, location='form', choices=('admin', 'member'), help="Role must be either 'admin' or 'member'")

userModel = api.model('User', {
  'id': fields.Integer(required=False),
  'username': fields.String(required=True),
  'role': fields.String(required=True)
})

userResponseModel = api.model('UserResponse', {
  'message': fields.String(description='Response message'),
  'result': fields.Nested(userModel)
})

@api.route('')
class Users(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.marshal_list_with(userResponseModel)
  def get(self):
    return UserController.index()
  
  @api.response(201, 'User has been created')
  @api.response(401, 'Unauthorized')
  @api.response(422, 'Validation Error')
  @api.expect(parser, validate=True)
  @api.marshal_with(userModel, code=HTTPStatus.CREATED)
  def post(self):
    parser.parse_args()
    return UserController.create(request.form)

@api.route('/<id>')
class User(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'User not found')
  @api.marshal_with(userResponseModel)
  def get(self, id):
    return UserController.show(id)
  
  @api.response(200, 'User has been updated')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'User not found')
  @api.response(422, 'Validation Error')
  @api.expect(parser, validate=True)
  @api.marshal_with(userModel)
  def put(self, id):
    parser.parse_args()
    return UserController.update(id, request.form)

  @api.response(200, 'User has been deleted')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'User not found')
  def delete(self, id):
    return UserController.delete(id)