from app.services import BookService

def index():
  return BookService.get_books()

def show(id):
  return BookService.get_book(id)

def create(data):
  return BookService.create_book(data)

def update(id, data):
  return BookService.update_book(id, data)

def delete(id):
  return BookService.delete_book(id)

def getAvailableBooks():
  return BookService.getAvailableBooks()

def updateAvailableBook(id, data):
  return BookService.updateAvailableBook(id, data)