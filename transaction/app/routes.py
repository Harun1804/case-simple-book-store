from app import app
from flask import request
from app.controllers import TransactionController

@app.route('/', methods=['GET'])
def index():
  return 'Harun Tampan'

@app.route('/transactions', methods=['GET','POST'])
def transactions():
  if request.method == 'GET':
    return TransactionController.index()
  elif request.method == 'POST':
    return TransactionController.store()

@app.route('/transactions/<id>', methods=['GET','PUT','DELETE'])
def transaction(id):
  if request.method == 'GET':
    return TransactionController.show(id)
  elif request.method == 'PUT':
    return TransactionController.update(id)
  elif request.method == 'DELETE':
    return TransactionController.delete(id)