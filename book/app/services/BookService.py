from app import db
from app.models.book import Book
from app.utils import formatter

def getBooks():
  books = Book.query.all()
  data = formatter.formatArray(books, singleTransform)
  return data

def getBook(id):
  book = Book.query.filter_by(id=id).first()
  data = singleTransform(book)
  return data

def storeBook(title, author, publisher, year, is_available):
  book = Book(title=title, author=author, publisher=publisher, year=year, is_available=False if is_available == '0' else True)
  db.session.add(book)
  db.session.commit()

def updateBook(id, title, author, publisher, year, is_available):
  book = Book.query.filter_by(id=id).first()
  book.title = title
  book.author = author
  book.publisher = publisher
  book.year = year
  book.is_available = False if is_available == '0' else True
  db.session.commit()

def deleteBook(id):
  book = Book.query.filter_by(id=id).first()
  if not book:
    return False
  db.session.delete(book)
  db.session.commit()

def singleTransform(data):
  data = {
    'id': data.id,
    'title': data.title,
    'author': data.author,
    'publisher': data.publisher,
    'year': data.year,
    'is_available': data.is_available,
  }

  return data