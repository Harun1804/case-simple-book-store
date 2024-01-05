from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from app.controllers import TransactionController
from http import HTTPStatus

api = Namespace('Transaction', description='Transaction service from transaction microservice')
parser = reqparse.RequestParser()
parser.add_argument('status', type=str, required=True, location='form', choices=('borrowed', 'returning'), help="Status must be either 'borrowed' or 'returning'")

transactionModel = api.model('Transaction', {
  'id': fields.Integer(required=False),
  'status': fields.String(required=True),
  'invoice': fields.String(required=True),
  'transaction_date': fields.DateTime(required=True),
  'due_date': fields.DateTime(required=True),
  'borrower_date': fields.DateTime(required=True),
  'return_date': fields.DateTime(required=False),
  'details': fields.List(fields.Nested(api.model('TransactionDetail', {
    'id': fields.Integer(required=False),
    'title': fields.String(required=True),
    'author': fields.String(required=True),
    'publisher': fields.String(required=True),
    'year': fields.Integer(required=True),
    'is_available': fields.Boolean(required=True)
  })))
})

transactionResponseModel = api.model('TransactionResponse', {
  'message': fields.String(description='Response message'),
  'result': fields.Nested(transactionModel)
})

transactionFormModel = api.model('TransactionForm', {
  'user_id': fields.Integer(required=True),
  'borrower_date': fields.DateTime(required=True),
  'books': fields.List(fields.Integer(required=True))
})

@api.route('')
class Transactions(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.marshal_list_with(transactionResponseModel)
  def get(self):
    return TransactionController.index()
  
  @api.response(201, 'Transaction has been created')
  @api.response(401, 'Unauthorized')
  @api.response(422, 'Validation Error')
  @api.expect(transactionFormModel, validate=True)
  @api.marshal_with(transactionModel, code=HTTPStatus.CREATED)
  def post(self):
    return TransactionController.create(request.json)

@api.route('/<id>')
class Transaction(Resource):
  @api.response(200, 'Success')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'Transaction not found')
  @api.marshal_with(transactionResponseModel)
  def get(self, id):
    return TransactionController.show(id)
  
  @api.response(200, 'Transaction has been updated')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'Transaction not found')
  @api.response(422, 'Validation Error')
  @api.expect(parser, validate=True)
  @api.marshal_with(transactionModel)
  def put(self, id):
    parser.parse_args()
    return TransactionController.update(id, request.form)

  @api.response(200, 'Transaction has been deleted')
  @api.response(401, 'Unauthorized')
  @api.response(404, 'Transaction not found')
  def delete(self, id):
    return TransactionController.delete(id)