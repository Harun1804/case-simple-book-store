from app import db
from app.models.book import Book
from app.utils import formatter
from app.utils import minio
import uuid

def getBooks():
  books = Book.query.all()
  data = formatter.formatArray(books, singleTransform)
  return data

def getAvailableBooks():
  books = Book.query.filter_by(is_available=True).all()
  data = formatter.formatArray(books, singleTransform)
  return data

def getBook(id):
  book = Book.query.filter_by(id=id).first()
  if not book:
    return False
  data = singleTransform(book)
  return data

def storeBook(title, author, publisher, year, is_available, thumbnail):
  thumbnail_name = filenameGenerator()
  minio.uploadFile(thumbnail, 'book', thumbnail_name)
  book = Book(title=title, author=author, publisher=publisher, year=year, is_available=False if is_available == '0' else True, thumbnail=thumbnail_name)
  db.session.add(book)
  db.session.commit()

def updateBook(id, title, author, publisher, year, is_available, thumbnail=None):
  book = Book.query.filter_by(id=id).first()
  if thumbnail:
    thumbnail_name = filenameGenerator()
    minio.updateFile(thumbnail, 'book', thumbnail_name, book.thumbnail)

  book.title = title
  book.author = author
  book.publisher = publisher
  book.year = year
  book.is_available = False if is_available == '0' else True
  if thumbnail:
    book.thumbnail = thumbnail_name

  db.session.commit()

def updateBookAvailability(id, is_available):
  book = Book.query.filter_by(id=id).first()
  book.is_available = False if is_available == '0' else True
  db.session.commit()

def deleteBook(id):
  book = Book.query.filter_by(id=id).first()
  minio.deleteFile('book', book.thumbnail)
  if not book:
    return False
  db.session.delete(book)
  db.session.commit()

def singleTransform(data):
  file = None
  if data.thumbnail:
    file = minio.getFileUrl('book', data.thumbnail)

  data = {
    'id': data.id,
    'title': data.title,
    'author': data.author,
    'publisher': data.publisher,
    'year': data.year,
    'is_available': data.is_available,
    'thumbnail' : file
  }

  return data

def filenameGenerator():
  return str(uuid.uuid4())