from app.utils import response
from flask import request
from app.services import BookService
from app.validations import StoreBookValidation, UpdateBookValidation, UpdateBookAvailabilityValidation

def index():
  try:
    books = BookService.getBooks()
    return response.success(books, "Success Get Books")
  except Exception as e:
    return response.error(str(e))

def show(id):
  try:
    book = BookService.getBook(id)
    if not book:
      return response.error("Book Not Found", 404)
    return response.success(book, "Success Get Book")
  except Exception as e:
    return response.error(str(e))

def available():
  try:
    books = BookService.getAvailableBooks()
    return response.success(books, "Success Get Available Books")
  except Exception as e:
    return response.error(str(e))

def updateAvailability(id):
  try:
    book = BookService.getBook(id)
    if not book:
      return response.error("Book Not Found", 404)

    validation = UpdateBookAvailabilityValidation.UpdateBookAvailableValidation().validate(request.form)
    if validation:
      return response.validateError(validation)

    is_available = request.form.get('is_available')
    BookService.updateBookAvailability(id, is_available)
    return response.success([], "Book Availability Has Been Updated")
  except Exception as e:
    return response.error(str(e))

def store():
  try:
    validation = StoreBookValidation.StoreBookValidation().validate(request.form)
    if validation:
      return response.validateError(validation)

    title = request.form.get('title')
    author = request.form.get('author')
    publisher = request.form.get('publisher')
    year = request.form.get('year')
    is_available = request.form.get('is_available')
    BookService.storeBook(title, author, publisher, year, is_available)
    return response.success([], "Book Has Been Created")
  except Exception as e:
    return response.error(str(e))

def update(id):
  try:
    book = BookService.getBook(id)
    if not book:
      return response.error("Book Not Found", 404)

    validation = UpdateBookValidation.UpdateBookValidation().validate(request.form)
    if validation:
      return response.validateError(validation)

    title = request.form.get('title')
    author = request.form.get('author')
    publisher = request.form.get('publisher')
    year = request.form.get('year')
    is_available = request.form.get('is_available')
    BookService.updateBook(id, title, author, publisher, year, is_available)
    return response.success([], "Book Has Been Updated")
  except Exception as e:
    return response.error(str(e))

def delete(id):
  try:
    book = BookService.getBook(id)
    if not book:
      return response.error("Book Not Found", 404)
    BookService.deleteBook(id)
    return response.success([], "Book Has Been Deleted")
  except Exception as e:
    return response.error(str(e))