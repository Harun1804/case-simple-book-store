from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from app.controllers import AuthController
from http import HTTPStatus

api = Namespace('Auth', description='Auth service from bookstore microservice')
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, location='form')
parser.add_argument('password', type=str, required=True, location='form')

authModel = api.model('Auth', {
  'username': fields.String(required=True),
  'role': fields.String(required=True)
})

loginModel = api.model('Login', {
  "access_token": fields.String(required=True),
  "refresh_token": fields.String(required=True),
  "status": fields.Boolean(required=True),
  "type": fields.String(required=True),
  "user": authModel
})

authResponseModel = api.model('AuthResponse', {
  'message': fields.String(description='Response message'),
  'result': authModel
})

loginResponseModel = api.model('LoginResponse', {
  'message': fields.String(description='Response message'),
  'result': loginModel
})

@api.route('/login')
class Login(Resource):
  @api.response(200, 'Success')
  @api.response(422, 'Validation Error')
  @api.expect(parser, validate=True)
  @api.marshal_with(authResponseModel)
  def post(self):
    parser.parse_args()
    return AuthController.login(request.form)

@api.route('/user')
class User(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.marshal_with(authResponseModel)
  def get(self):
    return AuthController.userLogin()