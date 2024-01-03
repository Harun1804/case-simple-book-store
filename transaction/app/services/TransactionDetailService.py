from app import db
from app.models.transaction_detail import TransactionDetail
from app.utils import formatter

def getTransactionDetails(transaction_id):
  transaction_details = TransactionDetail.query.filter((TransactionDetail.transaction_id == transaction_id))
  data = formatter.formatArray(transaction_details, singleTransform)
  return data

def storeTransactionDetail(transaction_id, books):
  book_ids = []
  for book in books:
    book_ids.extend([int(book_id) for book_id in book.split(',')])
  for book_id in book_ids:
    transaction_detail = TransactionDetail(book_id=book_id, transaction_id=transaction_id)
    db.session.add(transaction_detail)
  db.session.commit()

def singleTransform(data):
  data = {
    'id': data.id,
    'transaction_id': data.transaction_id,
    'book_id': data.book_id
  }

  return data