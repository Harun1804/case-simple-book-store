from app import db
from app.models.transaction import Transaction
from app.utils import formatter
from datetime import datetime, timedelta
from app.services.TransactionDetailService import storeTransactionDetail, getTransactionDetails
from datetime import datetime
import random
from app.services.BookService import updateBookAvailability

def getTransactions():
  transactions = Transaction.query.all()
  detailed_transactions = formatter.formatArray(transactions, lambda transaction: getTransaction(transaction.id))
  return detailed_transactions

def getTransaction(id):
  transaction = Transaction.query.filter_by(id=id).first()
  if not transaction:
    return False
  transaction_details = getTransactionDetails(transaction.id)
  data = singleTransform(transaction, transaction_details)
  return data

def storeTransaction(user_id, borrower_date, books):
  date = datetime.strptime(borrower_date, "%d-%m-%Y")
  invoice = generate_invoice()
  transaction = Transaction(invoice=invoice, user_id=user_id, transaction_date=datetime.utcnow(), borrower_date=date, due_date=date + timedelta(days=5), status='borrowed')
  db.session.add(transaction)
  db.session.commit()
  storeTransactionDetail(transaction.id, books)

def updateTransaction(id, status):
  transaction = Transaction.query.filter_by(id=id).first()
  transaction.return_date = datetime.utcnow()
  transaction.status = status
  details = getTransactionDetails(id)
  for detail in details:
    updateBookAvailability(detail['id'], 1)
  db.session.commit()

def deleteTransaction(id):
  transaction = Transaction.query.filter_by(id=id).first()
  if not transaction:
    return False
  db.session.delete(transaction)
  db.session.commit()

def singleTransform(transaction, details):
  keys = ['id', 'invoice', 'transaction_date', 'borrower_date', 'due_date', 'return_date', 'status']
  data = {key: getattr(transaction, key) for key in keys}
  data['details'] = details
  return data

def generate_invoice():
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    random_number = random.randint(100, 999)
    invoice = f"TRS-{current_date}-{random_number}"
    return invoice