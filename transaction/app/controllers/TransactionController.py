from app.utils import response
from flask import request
from app.services import TransactionService
from app.Validations import StoreTransactionValidation, UpdateTransactionValidation

def index():
  try:
    data = TransactionService.getTransactions()
    return response.success(data)
  except Exception as e:
    return response.error(str(e))

def show(id):
  try:
    data = TransactionService.getTransaction(id)
    if not data:
      return response.error("Transaction Not Found", 404)
    return response.success(data)
  except Exception as e:
    return response.error(str(e))

def store():
  try:
    validation = StoreTransactionValidation.StoreTransactionValidation().validate(request.json)
    if validation:
      return response.validateError(validation)

    user_id = request.json['user_id']
    borrower_date = request.json['borrower_date']
    books = request.json['books']
    TransactionService.storeTransaction(user_id, borrower_date, books)
    return response.success([], "Transaction Has Been Created")
  except Exception as e:
    return response.error(str(e))

def update(id):
  try:
    validation = UpdateTransactionValidation.UpdateTransactionValidation().validate(request.form)
    if validation:
      return response.validateError(validation)

    status = request.form.get('status')
    TransactionService.updateTransaction(id, status)
    return response.success([], "Transaction Has Been Updated")
  except Exception as e:
    return response.error(str(e))

def delete(id):
  try:
    data = TransactionService.getTransaction(id)
    if not data:
      return response.error("Transaction Not Found", 404)
    TransactionService.deleteTransaction(id)
    return response.success([], "Transaction Has Been Deleted")
  except Exception as e:
    return response.error(str(e))