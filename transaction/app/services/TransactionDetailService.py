from app import db
from app.models.transaction_detail import TransactionDetail
from app.utils import formatter
from app.services.BookService import updateBookAvailability, getBookById

def getTransactionDetails(transaction_id):
  transaction_details = TransactionDetail.query.filter((TransactionDetail.transaction_id == transaction_id))
  data = formatter.formatArray(transaction_details, lambda transaction_details: getBookById(transaction_details.book_id))
  return data

def storeTransactionDetail(transaction_id, books):
  book_ids = []
  for book in books:
    book_ids.extend([int(book_id) for book_id in book.split(',')])
  for book_id in book_ids:
    transaction_detail = TransactionDetail(book_id=book_id, transaction_id=transaction_id)
    updateBookAvailability(book_id, 0)
    db.session.add(transaction_detail)
  db.session.commit()

def singleTransform(data, book):
  keys = ['id', 'transaction_id', 'book_id'];
  data = {key: getattr(data, key) for key in keys}
  data['book'] = book

  return data