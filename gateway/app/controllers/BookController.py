from app.services import BookService

def index():
  return BookService.get_books()

def show(id):
  return BookService.get_book(id)

def create(data, files):
  return BookService.create_book(data, files)

def update(id, data, files=None):
  if files is None:
    return BookService.update_book(id, data)
  return BookService.update_book(id, data, files)

def delete(id):
  return BookService.delete_book(id)

def getAvailableBooks():
  return BookService.getAvailableBooks()

def updateAvailableBook(id, data):
  return BookService.updateAvailableBook(id, data)