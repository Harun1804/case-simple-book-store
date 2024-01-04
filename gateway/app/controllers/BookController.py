from app.services import BookService

def index():
  return BookService.get_books()