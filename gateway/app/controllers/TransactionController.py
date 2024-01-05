from app.services import TransactionService

def index():
  return TransactionService.getTransactions()

def show(id):
  return TransactionService.getTransaction(id)

def create(data):
  return TransactionService.storeTransaction(data)

def update(id, data):
  return TransactionService.updateTransaction(id, data)

def delete(id):
  return TransactionService.deleteTransaction(id)